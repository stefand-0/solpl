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

    def _has_guard(self, line):
        in_quote = False
        quote_char = None
        for char in line:
            if char in ['"', "'"]:
                if not in_quote:
                    in_quote = True
                    quote_char = char
                elif char == quote_char:
                    in_quote = False
                    quote_char = None
            elif not in_quote and char == '?':
                return True
        return False

    def _split_on_op(self, string, op):
        in_quote = False
        quote_char = None
        for i, char in enumerate(string):
            if char in ['"', "'"]:
                if not in_quote:
                    in_quote = True
                    quote_char = char
                elif char == quote_char:
                    in_quote = False
                    quote_char = None
            elif not in_quote and char == op:
                return string[:i], string[i+1:]
        return None, None

    def _split_outside_quotes(self, string, op):
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

    def _find_last_op(self, string, op):
        in_quote = False
        quote_char = None
        last_idx = -1
        for i, char in enumerate(string):
            if char in ['"', "'"]:
                if not in_quote:
                    in_quote = True
                    quote_char = char
                elif char == quote_char:
                    in_quote = False
                    quote_char = None
            elif not in_quote and char == op:
                last_idx = i
        return last_idx

    def _compute(self, expr):
        expr = str(expr).strip()
        # Handle parentheses
        idx = 0
        while True:
            end_idx = expr.find(')', idx)
            if end_idx == -1:
                break
            start_idx = expr.rfind('(', 0, end_idx)
            if start_idx == -1:
                break
            if start_idx > 0 and (expr[start_idx - 1].isalnum() or expr[start_idx - 1] == '_'):
                idx = end_idx + 1
                continue
            inner_expr = expr[start_idx + 1:end_idx]
            inner_result = self._compute(inner_expr)
            expr = expr[:start_idx] + str(inner_result) + expr[end_idx + 1:]
            idx = 0
        # String concatenation with +
        plus_parts = self._split_outside_quotes(expr, '+')
        if len(plus_parts) > 1:
            is_string_concat = False
            for p in plus_parts:
                p = p.strip()
                if (p.startswith('"') and p.endswith('"')) or (p.startswith("'") and p.endswith("'")):
                    is_string_concat = True
                    break
            if is_string_concat:
                result = ""
                for p in plus_parts:
                    val = self._resolve(p.strip())
                    result += str(val) if val is not None else ""
                return result
        # Equality comparison (=)
        left, right = self._split_on_op(expr, '=')
        if left is not None:
            r1 = self._resolve(left.strip())
            r2 = self._resolve(right.strip())
            if r1 is not None and r2 is not None:
                return 1 if r1 == r2 else 0
        # + and -
        for op in ['+', '-']:
            idx = self._find_last_op(expr, op)
            if idx != -1:
                left = expr[:idx].strip()
                right = expr[idx+1:].strip()
                r1 = self._resolve(left)
                r2 = self._resolve(right)
                if r1 is None or r2 is None:
                    continue
                val1 = float(r1)
                val2 = float(r2)
                if op == '+': return val1 + val2
                if op == '-': return val1 - val2
        # * and :
        last_idx = -1
        last_op = None
        for op in ['*', ':']:
            idx = self._find_last_op(expr, op)
            if idx > last_idx:
                last_idx = idx
                last_op = op
        if last_idx != -1:
            left = expr[:last_idx].strip()
            right = expr[last_idx+1:].strip()
            r1 = self._resolve(left)
            r2 = self._resolve(right)
            if r1 is None or r2 is None:
                pass
            else:
                val1 = float(r1)
                val2 = float(r2)
                if last_op == '*': return val1 * val2
                if last_op == ':': return val1 / val2
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
        if val.endswith("{}") and "{" not in val[:-2]:
            struct_name = val[:-2].strip()
            blueprint = self.struct_blueprints.get(struct_name)
            if blueprint is not None:
                return blueprint.copy()
            obj = self._lookup(struct_name)
            if isinstance(obj, dict):
                return obj.copy()
        if "(" in val and val.endswith(")") and not val.startswith("_"):
            parts = val.split("(", 1)
            name = parts[0].strip()
            if name in self.functions:
                args_str = parts[1][:-1].strip()
                args = [self._compute(a.strip()) for a in args_str.split(",")] if args_str else []
                return self._call_function(name, args)
            for func_name in self.functions:
                if func_name.endswith("." + name):
                    args_str = parts[1][:-1].strip()
                    args = [self._compute(a.strip()) for a in args_str.split(",")] if args_str else []
                    return self._call_function(func_name, args)
        if "[" in val and "]" in val:
            try:
                name, idx_part = val.split("[", 1)
                idx = int(idx_part.replace("]", "").strip())
                container = self._lookup(name)
                if isinstance(container, list): return container[idx]
            except (ValueError, IndexError, KeyError): pass
        if "." in val:
            parts = val.split(".")
            obj = self._lookup(parts[0])
            for part in parts[1:]:
                if isinstance(obj, dict):
                    obj = obj.get(part, 0)
                else:
                    return 0
            return obj
        for scope in reversed(self.scope_stack):
            if val in scope: return scope[val]
        if val in self.functions:
            return ("func_ref", val)
        for func_name in self.functions:
            if func_name.endswith("." + val):
                return ("func_ref", func_name)
        if val.replace('.', '', 1).isdigit() or (val.startswith('-') and val[1:].replace('.', '', 1).isdigit()):
            return float(val) if '.' in val else int(val)
        return None 

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
        left, right = self._split_on_op(cond, "=")
        if left is not None:
            return self._compute(cond)
        left, right = self._split_on_op(cond, "<")
        if left is not None:
            return self._compute(left.strip()) < self._compute(right.strip())
        left, right = self._split_on_op(cond, ">")
        if left is not None:
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
                if l.startswith(';'): continue
                if l.startswith('//'): continue
                if ';' in l:
                    l = l.split(';', 1)[0].strip()
                if l:
                    lines.append(l)
            # Parse structs first
            for pc, line in enumerate(lines):
                if line.endswith("{}") and "->" not in line and ">>" not in line and "?" not in line and not line.startswith("_"):
                    struct_name = line.split("{}")[0].strip()
                    fields = {}
                    npc = pc + 1
                    while npc < len(lines) and lines[npc] != "end":
                        if "->" in lines[npc]:
                            key, val = [x.strip() for x in lines[npc].split("->")]
                            fields[key] = self._resolve(val)
                        npc += 1
                    self.struct_blueprints[struct_name] = fields
                    self.variables[struct_name] = fields.copy()
            # Parse functions
            for pc, line in enumerate(lines):
                if "(" in line and ")" in line and "main" not in line and "end" not in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith(("if ", "while ", "for ", "elseif", "else")):
                    parts = line.split("(")
                    name = parts[0].strip()
                    params_str = parts[1].replace(")", "").strip()
                    params = [p.strip() for p in params_str.split(",")] if params_str else []
                    self.functions[f"{module_name}.{name}"] = {"start_pc": pc + 1, "params": params, "source_lines": lines}

    def execute(self, code):
        raw_lines = code.split('\n')
        self.lines = []
        for l in raw_lines:
            l = l.strip()
            if not l: continue
            if l.startswith(';'): continue
            if l.startswith('//'): continue
            if ';' in l:
                l = l.split(';', 1)[0].strip()
            if l:
                self.lines.append(l)
        self.threads = []
        pc = 0
        depth = 0
        while pc < len(self.lines):
            line = self.lines[pc]
            if line == "end":
                depth -= 1
                pc += 1
                continue
            if depth == 0 and "(" in line and ")" in line and "main" not in line and "end" not in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith(("if ", "while ", "for ", "elseif", "else")):
                parts = line.split("(")
                func_name = parts[0].strip()
                if not func_name.startswith("_"):
                    self.functions[func_name] = {"start_pc": pc + 1, "params": [p.strip() for p in parts[1].replace(")", "").split(",")] if parts[1].replace(")", "").strip() else []}
                    depth += 1
            elif depth == 0 and line.endswith("{}") and "->" not in line and ">>" not in line and "?" not in line and not line.startswith("_"):
                pc = self._parse_struct(pc)
                pc += 1
                continue
            elif depth > 0 and line.startswith(("if ", "while ", "for ")):
                depth += 1
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
        self.variables[struct_name] = fields.copy()
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
        local_scope = {}
        for p, a in zip(params, args):
            local_scope[p] = a
        self.scope_stack.append(local_scope)
        try: self._run_block(start_pc)
        except ReturnSignal as sig: return sig.value
        finally: self.scope_stack.pop()
        return 0

    def _execute_line(self, line):
        if line.startswith("_get("):
            filename = line.split('"')[1]
            self._import_file(filename)
            return
        if line.startswith("_call("):
            inner = line[6:-1].strip()
            parts = [p.strip() for p in inner.split(",")]
            func_name = self._resolve(parts[0])
            if isinstance(func_name, tuple) and func_name[0] == "func_ref":
                func_name = func_name[1]
            args = [self._compute(p) for p in parts[1:]]
            return self._call_function(func_name, args)
        if ">>" in line and "_in" in line:
            parts = [p.strip() for p in line.split(">>")]
            if len(parts) >= 3 and parts[1] == "_in":
                prompt = str(self._compute(parts[0]))
                var_name = parts[2]
                sys.stdout.write(prompt + " "); sys.stdout.flush()
                val = sys.stdin.readline().strip()
                try: self._assign(var_name, float(val) if '.' in val else int(val))
                except: self._assign(var_name, val)
                return
        is_async = False
        if ">>" in line:
            parts = [p.strip() for p in line.split(">>")]
            if parts[-1] == "_async":
                line = ">>".join(line.split(">>")[:-1]).strip()
                is_async = True
        if line.startswith("_return ->"):
            raise ReturnSignal(self._compute(line.split("->", 1)[1]))
        if ">>" in line and "_out" in line:
            parts = [p.strip() for p in line.split(">>")]
            if len(parts) == 2 and parts[1] == "_out":
                val = self._compute(parts[0])
                if is_async:
                    t = threading.Thread(target=lambda v=val: print(v if v is not None else ""))
                    t.start(); self.threads.append(t)
                else:
                    print(val if val is not None else "")
                return
        if line.startswith("_out"):
            val = self._compute(line.split("->", 1)[1].strip())
            if is_async:
                t = threading.Thread(target=lambda v=val: print(v if v is not None else ""))
                t.start(); self.threads.append(t)
            else:
                print(val if val is not None else "")
            return
        if line.startswith("_in"):
            if "->" in line:
                var_name = line.split("->", 1)[1].strip()
                sys.stdout.write(f"Input {var_name}: "); sys.stdout.flush()
                val = sys.stdin.readline().strip()
                try: self._assign(var_name, float(val) if '.' in val else int(val))
                except: self._assign(var_name, val)
            return
        if "_add(" in line:
            parts = [p.strip() for p in line.replace("_add(", "").replace(")", "").split(",")]
            container = self._lookup(parts[0])
            if isinstance(container, list): container.insert(int(parts[1]), self._resolve(parts[2]))
            return
        if "_remove(" in line:
            parts = [p.strip() for p in line.replace("_remove(", "").replace(")", "").split(",")]
            container = self._lookup(parts[0])
            if isinstance(container, list): container.pop(int(parts[1]))
            return
        if "_listen(" in line:
            p, h = [p.strip() for p in line.replace("_listen(", "").replace(")", "").split(",")]
            self._native_listen(self._compute(p), h)
            return
        if "<" in line and ">" in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith("_"):
            parts = line.split("<")
            if len(parts) == 2 and ">" in parts[1]:
                list_name = parts[1].split(">")[0].strip()
                self._assign(list_name, [])
                return
        if "->" in line:
            var, val = [x.strip() for x in line.split("->", 1)]
            if "." in var:
                parts = var.split(".")
                target = self._lookup(parts[0])
                if isinstance(target, dict):
                    for part in parts[1:-1]:
                        if isinstance(target, dict) and part in target:
                            target = target[part]
                        else:
                            target = None
                            break
                    if target is not None and isinstance(target, dict):
                        target[parts[-1]] = self._compute(val)
            else:
                computed = self._compute(val)
                self._assign(var, computed)
            return
        if "(" in line and line.endswith(")") and not line.startswith("_"):
            parts = line.split("(")
            func_name = parts[0].strip()
            args_str = parts[1][:-1].strip()
            args = [self._compute(a.strip()) for a in args_str.split(",")] if args_str else []
            if is_async:
                t = threading.Thread(target=self._call_function, args=(func_name, args))
                t.start(); self.threads.append(t)
            else:
                self._call_function(func_name, args)
            return

    def _run_block(self, start_pc):
        pc = start_pc
        control_stack = [] 
        while pc < len(self.lines):
            line = self.lines[pc]
            is_executing = all(level["executing"] for level in control_stack)
            if is_executing and "(" in line and ")" in line and "main" not in line and "end" not in line and "->" not in line and ">>" not in line and "?" not in line and not line.startswith(("if ", "while ", "for ", "elseif", "else")):
                func_candidate = line.split("(")[0].strip()
                if func_candidate in self.functions:
                    depth = 1
                    npc = pc + 1
                    while npc < len(self.lines) and depth > 0:
                        if self.lines[npc].startswith(("if ", "while ", "for ")):
                            depth += 1
                        elif self.lines[npc] == "end":
                            depth -= 1
                        npc += 1
                    pc = npc
                    continue
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
                range_parts = parts[1].split(" to ")
                start_v = int(self._compute(range_parts[0].strip()))
                end_v = int(self._compute(range_parts[1].strip()))
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
                if self._has_guard(line):
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