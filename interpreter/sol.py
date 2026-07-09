import threading
import time
import sys
import os
import urllib.request
import http.server

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class SolInterpreter:
    def __init__(self):
        self.variables = {}
        self.thread_local = threading.local()
        self.functions = {}
        self.struct_blueprints = {} 
        self.lines = []
        self.threads = []
        self._server_started = False 

    @property
    def scope_stack(self):
        if not hasattr(self.thread_local, "stack"):
            self.thread_local.stack = [self.variables]
        return self.thread_local.stack

    def _import_file(self, filename):
        if not os.path.exists(filename):
            print(f"Error: Module '{filename}' not found.")
            return

        with open(filename, "r") as f:
            code = f.read()
            module_name = os.path.splitext(os.path.basename(filename))[0]

            lines = []
            for l in code.split('\n'):
                l = l.strip()
                if not l: continue
                if ';' in l:
                    l = l.split(';', 1)[0].strip()
                if l:
                    lines.append(l)

            for pc, line in enumerate(lines):
                if "(" in line and ")" in line and "main" not in line and "end" not in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith(("if ", "while ", "for ", "elseif", "else")):
                    parts = line.split("(")
                    name = parts[0].strip()
                    params_str = parts[1].replace(")", "").strip()
                    params = [p.strip() for p in params_str.split(",")] if params_str else []
                    self.functions[f"{module_name}.{name}"] = {"start_pc": pc + 1, "params": params, "source_lines": lines}

    def _compute(self, expr):
        expr = str(expr).strip()

        def split_outside_quotes(string, op):
            parts = []
            current = []
            in_quote = False
            quote_char = None
            for char in string:
                if char in ['"', "'"]:
                    if not in_quote:
                        in_quote = True
                        quote_char = char
                    elif char == quote_char:
                        in_quote = False
                        quote_char = None
                    current.append(char)
                elif not in_quote and char == op:
                    parts.append("".join(current))
                    current = []
                else:
                    current.append(char)
            parts.append("".join(current))
            return parts

        plus_parts = split_outside_quotes(expr, '+')
        if len(plus_parts) > 1:
            if any(any(c.isalpha() or c in ['"', "'"] for c in p) for p in plus_parts):
                result = ""
                for p in plus_parts:
                    val = self._resolve(p.strip())
                    result += str(val) if val is not None else ""
                return result

        ops = ['+', '-', '*', ':']
        for op in ops:
            op_parts = split_outside_quotes(expr, op)
            if len(op_parts) > 1:
                try:
                    left = op_parts[0]
                    right = op.join(op_parts[1:])
                    r1 = self._resolve(left.strip())
                    r2 = self._resolve(right.strip())
                    if r1 is None or r2 is None: continue
                    val1 = float(r1)
                    val2 = float(r2)
                    if op == '+': return val1 + val2
                    if op == '-': return val1 - val2
                    if op == '*': return val1 * val2
                    if op == ':': return val1 / val2
                except (ValueError, TypeError): continue
        return self._resolve(expr)

    def _lookup(self, name):
        for scope in reversed(self.scope_stack):
            if name in scope: return scope[name]
        return None

    def _assign(self, name, val):
        self.scope_stack[-1][name] = val

    def _resolve(self, val):
        val = str(val).strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            return val[1:-1]
        if val.startswith("_fetch(") and val.endswith(")"):
            url_expr = val[7:-1].strip()
            return self._native_fetch(str(self._compute(url_expr)))
        if "(" in val and val.endswith(")") and not val.startswith("_"):
            parts = val.split("(", 1)
            name = parts[0].strip()
            if name in self.functions:
                args_str = parts[1][:-1].strip()
                args = [self._compute(a.strip()) for a in args_str.split(",")] if args_str else []
                return self._call_function(name, args)
        if "[" in val and "]" in val:
            try:
                name, idx_part = val.split("[")
                idx = int(idx_part.replace("]", "").strip())
                container = self._lookup(name)
                if isinstance(container, list): return container[idx]
            except (ValueError, IndexError, KeyError): pass
        if "." in val:
            obj_name, prop = val.split(".", 1)
            obj = self._lookup(obj_name)
            if isinstance(obj, dict): return obj.get(prop, 0)

        for scope in reversed(self.scope_stack):
            if val in scope: return scope[val]

        # FIX: Only try to parse as number if it looks like one
        if val.replace('.', '', 1).isdigit() or (val.startswith('-') and val[1:].replace('.', '', 1).isdigit()):
            return float(val) if '.' in val else int(val)
        
        return None 

    def _async_worker(self, expr, action):
        result = self._compute(expr)
        if action == "_out": print(f"[ASYNC OUTPUT] {result}")

    def _async_input_worker(self, prompt, var_name):
        user_val = input(prompt)
        try:
            if '.' in user_val: user_val = float(user_val)
            else: user_val = int(user_val)
        except ValueError: pass
        self._assign(var_name, user_val)

    def _native_fetch(self, url):
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                return response.read().decode('utf-8', errors='replace')
        except Exception as e: return f"Error: {str(e)}"

    def _native_listen(self, port, handler_name):
        if self._server_started: return
        self._server_started = True
        interpreter_instance = self
        class SolHTTPHandler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                response_body = interpreter_instance._call_function(handler_name, [self.path])
                self.wfile.write(bytes(str(response_body), "utf-8"))
            def log_message(self, format, *args): pass 
        def server_thread():
            server = http.server.HTTPServer(("0.0.0.0", int(port)), SolHTTPHandler)
            server.serve_forever()
        t = threading.Thread(target=server_thread, daemon=True)
        t.start()
        self.threads.append(t)

    def _evaluate_condition(self, cond):
        if "==" in cond:
            left, right = cond.split("==", 1)
            return self._compute(left.strip()) == self._compute(right.strip())
        if "=" in cond:
            left, right = cond.split("=")
            return self._compute(left.strip()) == self._compute(right.strip())
        elif "<" in cond:
            left, right = cond.split("<")
            return self._compute(left.strip()) < self._compute(right.strip())
        elif ">" in cond:
            left, right = cond.split(">")
            return self._compute(left.strip()) > self._compute(right.strip())
        return False

    def _get_block_end(self, start_pc):
        depth = 1
        pc = start_pc + 1
        while pc < len(self.lines):
            line = self.lines[pc]
            if line.startswith("if ") or line.startswith("while ") or line.startswith("for "): depth += 1
            elif line == "end":
                depth -= 1
                if depth == 0: return pc
            pc += 1
        return pc

    def execute(self, code):
        self.lines = [l.strip() for l in code.split('\n') if l.strip() and ';' not in l or (';' in l and l.split(';', 1)[0].strip())]
        self.lines = [l.split(';', 1)[0].strip() for l in self.lines]
        self.threads = []
        pc = 0
        while pc < len(self.lines):
            line = self.lines[pc]
            if "(" in line and ")" in line and "main" not in line and "end" not in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith(("if ", "while ", "for ", "elseif", "else")):
                parts = line.split("(")
                self.functions[parts[0].strip()] = {"start_pc": pc + 1, "params": [p.strip() for p in parts[1].replace(")", "").split(",")] if parts[1].replace(")", "").strip() else []}
            elif "{" in line: pc = self._parse_struct(pc)
            pc += 1
        for i, line in enumerate(self.lines):
            if line == "main()":
                try: self._run_block(i + 1)
                except ReturnSignal: pass
                break
        for t in self.threads:
            if t.is_alive() and not t.daemon: t.join()

    def _parse_struct(self, pc):
        struct_name = self.lines[pc].split("{}")[0].strip()
        fields = {}
        pc += 1
        while pc < len(self.lines) and self.lines[pc] != "end":
            if "->" in self.lines[pc]:
                key, val = [x.strip() for x in self.lines[pc].split("->")]
                fields[key] = self._resolve(val)
            pc += 1
        self.struct_blueprints[struct_name] = fields
        self._assign(struct_name, fields.copy())
        return pc

    def _call_function(self, name, args):
        if "." in name and name in self.functions:
            orig_lines = self.lines
            self.lines = self.functions[name]["source_lines"]
            res = self._run_with_scope(self.functions[name]["start_pc"], self.functions[name]["params"], args)
            self.lines = orig_lines
            return res
        return self._run_with_scope(self.functions[name]["start_pc"], self.functions[name]["params"], args)

    def _run_with_scope(self, start_pc, params, args):
        local_scope = {p: a for p, a in zip(params, args)}
        self.scope_stack.append(local_scope)
        try: self._run_block(start_pc)
        except ReturnSignal as sig: return sig.value
        finally: self.scope_stack.pop()
        return 0

    def _execute_line(self, line):
        if "_get(" in line:
            filename = line.split('"')[1]
            self._import_file(filename)
            return
        if ">>" in line and "_input" in line:
            parts = [p.strip() for p in line.split(">>")]
            t = threading.Thread(target=self._async_input_worker, args=(str(self._compute(parts[0])), parts[2]))
            t.start(); self.threads.append(t); return
        is_async_func = ">>" in line and "_async" in line and "(" in line and not line.startswith("_")
        if is_async_func: line = line.split(">>")[0].strip()
        if line.startswith("_return ->"): raise ReturnSignal(self._compute(line.split("->", 1)[1]))
        elif ">>" in line and "_async" in line:
            parts = line.split(">>")
            t = threading.Thread(target=self._async_worker, args=(parts[0].strip(), parts[2].strip()))
            t.start(); self.threads.append(t)
        elif line.startswith("_in"):
            prompt = line.split('(')[1].split(')')[0].replace('"', '').replace("'", "") if "(" in line else f"Input {line.split('->')[1].strip()}: "
            sys.stdout.write(prompt + " "); sys.stdout.flush()
            val = sys.stdin.readline().strip()
            try: self._assign(line.split("->")[1].strip(), float(val) if '.' in val else int(val))
            except: self._assign(line.split("->")[1].strip(), val)
        elif "_add(" in line:
            parts = [p.strip() for p in line.replace("_add(", "").replace(")", "").split(",")]
            container = self._lookup(parts[0])
            if isinstance(container, list): container.insert(int(parts[1]), self._resolve(parts[2]))
        elif "_remove(" in line:
            parts = [p.strip() for p in line.replace("_remove(", "").replace(")", "").split(",")]
            container = self._lookup(parts[0])
            if isinstance(container, list): container.pop(int(parts[1]))
        elif "_listen(" in line:
            p, h = [p.strip() for p in line.replace("_listen(", "").replace(")", "").split(",")]
            self._native_listen(self._compute(p), h)
        elif "_out" in line:
            val = self._compute(line.split("->")[1].strip())
            print(val if val is not None else "Error")
        elif "mylist<" in line: self._assign(line.split("<")[1].split(">")[0], [])
        elif "->" in line:
            var, val = [x.strip() for x in line.split("->")]
            if "." in var:
                obj, prop = var.split(".", 1)
                target = self._lookup(obj)
                if isinstance(target, dict): target[prop] = self._compute(val)
            else: self._assign(var, self._compute(val))
        elif "(" in line and line.endswith(")") and not line.startswith("_"):
            parts = line.split("(")
            if is_async_func:
                t = threading.Thread(target=self._call_function, args=(parts[0].strip(), [self._compute(a.strip()) for a in parts[1].replace(")", "").split(",")]))
                t.start(); self.threads.append(t)
            else: self._call_function(parts[0].strip(), [self._compute(a.strip()) for a in parts[1].replace(")", "").split(",")])

    def _run_block(self, start_pc):
        pc = start_pc
        control_stack = [] 
        while pc < len(self.lines):
            line = self.lines[pc]
            is_executing = all(level["executing"] for level in control_stack)
            if line.startswith("if "):
                control_stack.append({"type": "if", "executing": is_executing and self._evaluate_condition(line.split("if ", 1)[1].strip()), "any_branch_true": False})
                pc += 1; continue
            elif line.startswith("elseif "):
                cond = line.split("elseif ", 1)[1].strip()
                parent_active = all(level["executing"] for level in control_stack[:-1]) if len(control_stack) > 1 else True
                if control_stack and control_stack[-1]["type"] == "if":
                    if parent_active and not control_stack[-1]["any_branch_true"] and self._evaluate_condition(cond):
                        control_stack[-1]["executing"] = True
                        control_stack[-1]["any_branch_true"] = True
                    else: control_stack[-1]["executing"] = False
                pc += 1; continue
            elif line == "else":
                parent_active = all(level["executing"] for level in control_stack[:-1]) if len(control_stack) > 1 else True
                if control_stack and control_stack[-1]["type"] == "if":
                    control_stack[-1]["executing"] = parent_active and not control_stack[-1]["any_branch_true"]
                pc += 1; continue
            elif line.startswith("while "):
                cond = line.split("while ", 1)[1].strip()
                end_pc = self._get_block_end(pc)
                if is_executing and self._evaluate_condition(cond):
                    control_stack.append({"type": "while", "executing": True, "start_pc": pc, "end_pc": end_pc})
                    pc += 1
                else: pc = end_pc + 1
                continue
            elif line.startswith("for "):
                parts = line.split("for ", 1)[1].split("->")
                var_name = parts[0].strip()
                start_v = int(self._compute(parts[1].split(" to ")[0].strip()))
                end_v = int(self._compute(parts[1].split(" to ")[1].strip()))
                end_pc = self._get_block_end(pc)
                if is_executing and start_v <= end_v:
                    self._assign(var_name, start_v)
                    control_stack.append({"type": "for", "executing": True, "var": var_name, "end_val": end_v, "start_pc": pc, "end_pc": end_pc})
                    pc += 1
                else: pc = end_pc + 1
                continue
            elif line == "end":
                if control_stack:
                    top = control_stack.pop()
                    if top.get("type") == "while" and top["executing"]: pc = top["start_pc"] - 1
                    elif top.get("type") == "for" and top["executing"]:
                        curr = self._lookup(top["var"]) + 1
                        if curr <= top["end_val"]:
                            self._assign(top["var"], curr)
                            pc = top["start_pc"] - 1
                pc += 1; continue
            if is_executing:
                if "?" in line:
                    cond, action = line.split("?", 1)
                    if self._evaluate_condition(cond.strip()): self._execute_line(action.strip())
                else: self._execute_line(line)
            pc += 1

def main():
    engine = SolInterpreter()
    if not sys.stdin.isatty():
        code = sys.stdin.read()
    elif len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f: code = f.read()
    else:
        print("Usage: solpl <file.sol> OR cat file.sol | python sol.py"); sys.exit(1)
    engine.execute(code)

if __name__ == "__main__":
    main()
