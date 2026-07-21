#!/usr/bin/env python3
"""
SOL Programming Language --
"""

import re
import sys
import os
import math
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple, Optional, Callable
from enum import Enum, auto

# ============================================================
# SECTION 1: STANDARD LIBRARY - I/O
# ============================================================

_last_error = ""

def std_out(val):
    print(val, end="")

def std_outln(val):
    print(val)

def std_in(prompt):
    return input(prompt)

def std_err(val):
    print(val, file=sys.stderr)

def std_quit(code):
    sys.exit(code)

def std_load(filename):
    global _last_error
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        _last_error = str(e)
        return ""

def std_save(filename, data):
    global _last_error
    try:
        with open(filename, 'w') as f:
            f.write(str(data))
    except Exception as e:
        _last_error = str(e)

def std_lasterr():
    return _last_error

def std_clearerr():
    global _last_error
    _last_error = ""

# ============================================================
# SECTION 2: STANDARD LIBRARY - STRING
# ============================================================

def string_upper(s):
    return s.upper()

def string_lower(s):
    return s.lower()

def string_has(s, ch):
    return ch in s

def string_nothave(s, ch):
    return ch not in s

def string_length(s):
    return len(s)

def string_isempty(s):
    return s is None or s == ""

def string_isnumeric(s):
    return bool(re.match(r'^[0-9]+$', str(s)))

def string_isalpha(s):
    return bool(re.match(r'^[a-zA-Z]+$', str(s)))

def string_isalphanum(s):
    return bool(re.match(r'^[a-zA-Z0-9]+$', str(s)))

def string_titlecase(s):
    return str(s).title()

def string_camelcase(s):
    words = re.split(r'[\s_\-]+', str(s))
    if not words or words == ['']:
        return ""
    return words[0].lower() + ''.join(w.capitalize() for w in words[1:])

def string_snakecase(s):
    return '_'.join(re.split(r'[\s\-]+', str(s)))

def string_kebabcase(s):
    return '-'.join(re.split(r'[\s_]+', str(s)))

def string_trim(s):
    return str(s).strip()

def string_trimleft(s):
    return str(s).lstrip()

def string_trimright(s):
    return str(s).rstrip()

# ============================================================
# SECTION 3: STANDARD LIBRARY - TYPE CONVERSIONS
# ============================================================

def type_toString(val):
    return str(val)

def type_strToInteger(s):
    try:
        return int(s)
    except:
        return False

def type_flToInt(f):
    return int(f)

def type_iToFloat(i):
    return float(i)

def type_iToHex(i):
    return f"0x{i:x}"

def type_iToOct(i):
    return f"0o{i:o}"

def type_octToInt(s):
    return int(s[2:], 8)

def type_hexToInt(s):
    return int(s[2:], 16)

def type_binaryToInt(s):
    return int(s[2:], 2)

def type_boolToInt(b):
    return 1 if b else 0

def type_intToBool(i):
    return i != 0

# ============================================================
# SECTION 4: STANDARD LIBRARY - LIST METHODS
# ============================================================

def list_push(lst, item):
    return lst + [item]

def list_pop(lst):
    if not lst:
        return [], False
    return lst[:-1], lst[-1]

def list_insert(lst, index, item):
    return lst[:index] + [item] + lst[index:]

def list_remove(lst, index):
    return lst[:index] + lst[index+1:]

def list_removeval(lst, item):
    result = lst.copy()
    if item in result:
        result.remove(item)
    return result

def list_find(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1

def list_sort(lst, cmp=None):
    return sorted(lst, key=cmp) if cmp else sorted(lst)

def list_reverse(lst):
    return lst[::-1]

def list_clear(lst):
    return []

def list_len(lst):
    return len(lst)

def list_copy(lst):
    return lst.copy()

def list_slice(lst, start, end):
    return lst[start:end]

def list_first(lst):
    return lst[0] if lst else False

def list_last(lst):
    return lst[-1] if lst else False

def list_contains(lst, item):
    return item in lst

# ============================================================
# SECTION 5: STANDARD LIBRARY - MAP METHODS
# ============================================================

def map_set(m, key, val):
    result = m.copy()
    result[key] = val
    return result

def map_get(m, key):
    return m.get(key, False)

def map_remove(m, key):
    result = m.copy()
    if key in result:
        del result[key]
    return result

def map_has(m, key):
    return key in m

def map_keys(m):
    return list(m.keys())

def map_values(m):
    return list(m.values())

def map_len(m):
    return len(m)

def map_clear(m):
    return {}

def map_contains(m, key):
    return key in m

# ============================================================
# SECTION 6: RESULT<T, E> TYPE
# ============================================================

@dataclass
class Ok:
    val: Any

@dataclass
class Err:
    msg: str

def result_isOk(r):
    return isinstance(r, Ok)

def result_isErr(r):
    return isinstance(r, Err)

def result_unwrap(r):
    if isinstance(r, Ok):
        return r.val
    raise RuntimeError(f"unwrap called on Err: {r.msg}")

def result_unwrapOr(r, default):
    return r.val if isinstance(r, Ok) else default

def result_unwrapOrElse(r, f):
    return r.val if isinstance(r, Ok) else f()

def result_expect(r, msg):
    if isinstance(r, Ok):
        return r.val
    raise RuntimeError(f"{msg}: {r.msg}")

def result_map(r, f):
    return Ok(f(r.val)) if isinstance(r, Ok) else r

def result_mapErr(r, f):
    return r if isinstance(r, Ok) else Err(f(r.msg))

def result_andThen(r, f):
    return f(r.val) if isinstance(r, Ok) else r

# ============================================================
# SECTION 7: VECTOR TYPE
# ============================================================

@dataclass
class SolVect:
    pairs: List[Tuple[Any, Any]]

# ============================================================
# SECTION 8: LEXER
# ============================================================

class TokenType(Enum):
    IDENT = auto()
    TYPE = auto()
    STRING = auto()
    CHAR = auto()
    NUMBER = auto()
    OCT = auto()
    BIN = auto()
    HEX = auto()
    BOOLEAN = auto()
    # Keywords
    IMM = auto(); NONIMM = auto(); FUN = auto(); LD = auto(); RET = auto()
    IF = auto(); ELSEIF = auto(); ELSE = auto(); END = auto()
    WHILE = auto(); FOR = auto(); BREAK = auto(); CONTINUE = auto()
    MATCH = auto(); WHEN = auto()
    TEMPL = auto(); DATA = auto(); INTERFACE = auto(); EXT = auto()
    MODULE = auto(); IMPORT = auto(); AS = auto()
    NULL = auto(); UNDEFINED = auto()
    OK = auto(); ERR = auto(); RESULT = auto()
    # Operators
    ARROW = auto(); COLON = auto(); SEMICOLON = auto(); COMMA = auto()
    DOT = auto(); QUESTION = auto(); BANG = auto()
    LPAREN = auto(); RPAREN = auto(); LBRACKET = auto(); RBRACKET = auto()
    LBRACE = auto(); RBRACE = auto()
    LT = auto(); GT = auto(); LE = auto(); GE = auto()
    EQ = auto(); NEQ = auto(); ASSIGN = auto()
    PLUS = auto(); MINUS = auto(); STAR = auto(); SLASH = auto()
    PERCENT = auto(); POWER = auto()
    AND = auto(); OR = auto(); NOT = auto()
    BITAND = auto(); BITOR = auto(); BITXOR = auto(); BITNOT = auto()
    LSHIFT = auto(); RSHIFT = auto()
    ELVIS = auto(); SAFE_ACCESS = auto()
    NEWLINE = auto(); EOF = auto()

KEYWORDS = {
    'imm': TokenType.IMM, 'nonimm': TokenType.NONIMM, 'fun': TokenType.FUN,
    'ld': TokenType.LD, 'ret': TokenType.RET,
    'if': TokenType.IF, 'elseif': TokenType.ELSEIF, 'else': TokenType.ELSE,
    'end': TokenType.END, 'while': TokenType.WHILE, 'for': TokenType.FOR,
    'break': TokenType.BREAK, 'continue': TokenType.CONTINUE,
    'match': TokenType.MATCH, 'when': TokenType.WHEN,
    'templ': TokenType.TEMPL, 'data': TokenType.DATA,
    'interface': TokenType.INTERFACE, 'ext': TokenType.EXT,
    'module': TokenType.MODULE, 'import': TokenType.IMPORT, 'as': TokenType.AS,
    'null': TokenType.NULL, 'undefined': TokenType.UNDEFINED,
    'nothing': TokenType.NULL,
    'Ok': TokenType.OK, 'Err': TokenType.ERR, 'Result': TokenType.RESULT,
    'true': TokenType.BOOLEAN, 'false': TokenType.BOOLEAN,
}

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    col: int

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []

    def error(self, msg):
        raise SyntaxError(f"{msg} at line {self.line}, col {self.col}")

    def peek(self, offset=0):
        p = self.pos + offset
        if p >= len(self.source):
            return '\0'
        return self.source[p]

    def advance(self):
        ch = self.source[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def skip_whitespace(self):
        while self.peek() in ' \t\r':
            self.advance()

    def read_string(self):
        self.advance()  # skip opening quote
        result = ""
        while self.peek() != '"' and self.peek() != '\0':
            if self.peek() == '\\':
                self.advance()
                ch = self.advance()
                if ch == 'n': result += '\n'
                elif ch == 't': result += '\t'
                elif ch == '\\': result += '\\'
                elif ch == '"': result += '"'
                else: result += ch
            else:
                result += self.advance()
        if self.peek() == '"':
            self.advance()
        return result

    def read_char(self):
        self.advance()  # skip opening quote
        ch = self.advance()
        if self.peek() == "'":
            self.advance()
        return ch

    def read_number(self):
        start = self.pos
        while self.peek().isdigit():
            self.advance()
        if self.peek() == '.' and self.peek(1).isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
            return float(self.source[start:self.pos])
        return int(self.source[start:self.pos])

    def read_hex(self):
        self.advance(); self.advance()  # skip 0x
        start = self.pos
        while self.peek() in '0123456789abcdefABCDEF':
            self.advance()
        return self.source[start-2:self.pos]

    def read_oct(self):
        self.advance(); self.advance()  # skip 0o
        start = self.pos
        while self.peek() in '01234567':
            self.advance()
        return self.source[start-2:self.pos]

    def read_bin(self):
        self.advance(); self.advance()  # skip 0b
        start = self.pos
        while self.peek() in '01':
            self.advance()
        return self.source[start-2:self.pos]

    def read_identifier(self):
        start = self.pos
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()
        return self.source[start:self.pos]

    def add_token(self, ttype, value=None):
        self.tokens.append(Token(ttype, value, self.line, self.col))

    def tokenize(self):
        while self.pos < len(self.source):
            self.skip_whitespace()
            if self.pos >= len(self.source):
                break

            ch = self.peek()
            line, col = self.line, self.col

            if ch == '\n':
                self.advance()
                self.add_token(TokenType.NEWLINE)
            elif ch == '/' and self.peek(1) == '/':
                while self.peek() != '\n' and self.peek() != '\0':
                    self.advance()
            elif ch == '/' and self.peek(1) == '*':
                self.advance(); self.advance()
                while not (self.peek() == '*' and self.peek(1) == '/'):
                    if self.peek() == '\0':
                        self.error("Unterminated block comment")
                    self.advance()
                self.advance(); self.advance()
            elif ch == '"':
                self.add_token(TokenType.STRING, self.read_string())
            elif ch == "'":
                self.add_token(TokenType.CHAR, self.read_char())
            elif ch == '0' and self.peek(1) == 'x':
                self.add_token(TokenType.HEX, self.read_hex())
            elif ch == '0' and self.peek(1) == 'o':
                self.add_token(TokenType.OCT, self.read_oct())
            elif ch == '0' and self.peek(1) == 'b':
                self.add_token(TokenType.BIN, self.read_bin())
            elif ch.isdigit():
                self.add_token(TokenType.NUMBER, self.read_number())
            elif ch.isalpha() or ch == '_':
                ident = self.read_identifier()
                if ident in KEYWORDS:
                    ttype = KEYWORDS[ident]
                    val = True if ident == 'true' else (False if ident == 'false' else ident)
                    self.add_token(ttype, val)
                else:
                    self.add_token(TokenType.IDENT, ident)
            elif ch == '-' and self.peek(1) == '>':
                self.advance(); self.advance()
                self.add_token(TokenType.ARROW)
            elif ch == '<' and self.peek(1) == '=':
                self.advance(); self.advance()
                self.add_token(TokenType.LE)
            elif ch == '>' and self.peek(1) == '=':
                self.advance(); self.advance()
                self.add_token(TokenType.GE)
            elif ch == '=' and self.peek(1) == '=':
                self.advance(); self.advance()
                self.add_token(TokenType.EQ)
            elif ch == '!' and self.peek(1) == '=':
                self.advance(); self.advance()
                self.add_token(TokenType.NEQ)
            elif ch == '*' and self.peek(1) == '*':
                self.advance(); self.advance()
                self.add_token(TokenType.POWER)
            elif ch == '&' and self.peek(1) == '&':
                self.advance(); self.advance()
                self.add_token(TokenType.AND)
            elif ch == '|' and self.peek(1) == '|':
                self.advance(); self.advance()
                self.add_token(TokenType.OR)
            elif ch == '?' and self.peek(1) == ':':
                self.advance(); self.advance()
                self.add_token(TokenType.ELVIS)
            elif ch == '?' and self.peek(1) == '.':
                self.advance(); self.advance()
                self.add_token(TokenType.SAFE_ACCESS)
            elif ch == '<' and self.peek(1) == '<':
                self.advance(); self.advance()
                self.add_token(TokenType.LSHIFT)
            elif ch == '>' and self.peek(1) == '>':
                self.advance(); self.advance()
                self.add_token(TokenType.RSHIFT)
            elif ch == ':': self.advance(); self.add_token(TokenType.COLON)
            elif ch == ';': self.advance(); self.add_token(TokenType.SEMICOLON)
            elif ch == ',': self.advance(); self.add_token(TokenType.COMMA)
            elif ch == '.': self.advance(); self.add_token(TokenType.DOT)
            elif ch == '?': self.advance(); self.add_token(TokenType.QUESTION)
            elif ch == '!': self.advance(); self.add_token(TokenType.BANG)
            elif ch == '(': self.advance(); self.add_token(TokenType.LPAREN)
            elif ch == ')': self.advance(); self.add_token(TokenType.RPAREN)
            elif ch == '[': self.advance(); self.add_token(TokenType.LBRACKET)
            elif ch == ']': self.advance(); self.add_token(TokenType.RBRACKET)
            elif ch == '{': self.advance(); self.add_token(TokenType.LBRACE)
            elif ch == '}': self.advance(); self.add_token(TokenType.RBRACE)
            elif ch == '<': self.advance(); self.add_token(TokenType.LT)
            elif ch == '>': self.advance(); self.add_token(TokenType.GT)
            elif ch == '+': self.advance(); self.add_token(TokenType.PLUS)
            elif ch == '-': self.advance(); self.add_token(TokenType.MINUS)
            elif ch == '*': self.advance(); self.add_token(TokenType.STAR)
            elif ch == '/': self.advance(); self.add_token(TokenType.SLASH)
            elif ch == '%': self.advance(); self.add_token(TokenType.PERCENT)
            elif ch == '&': self.advance(); self.add_token(TokenType.BITAND)
            elif ch == '|': self.advance(); self.add_token(TokenType.BITOR)
            elif ch == '^': self.advance(); self.add_token(TokenType.BITXOR)
            elif ch == '~': self.advance(); self.add_token(TokenType.BITNOT)
            elif ch == '=': self.advance(); self.add_token(TokenType.ASSIGN)
            else:
                self.error(f"Unexpected character: {ch}")

        self.add_token(TokenType.EOF)
        return self.tokens

# ============================================================
# SECTION 9: PARSER
# ============================================================

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def advance(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def expect(self, ttype):
        tok = self.peek()
        if tok.type != ttype:
            raise SyntaxError(f"Expected {ttype.name}, got {tok.type.name} at line {tok.line}")
        return self.advance()

    def match(self, *types):
        if self.peek().type in types:
            return self.advance()
        return None

    def skip_newlines(self):
        while self.peek().type == TokenType.NEWLINE:
            self.advance()

    def parse(self):
        stmts = []
        while self.peek().type != TokenType.EOF:
            self.skip_newlines()
            if self.peek().type == TokenType.EOF:
                break
            stmts.append(self.parse_stmt())
        return ('program', stmts)

    def parse_stmt(self):
        self.skip_newlines()
        tok = self.peek()
        if tok.type in (TokenType.IMM, TokenType.NONIMM):
            return self.parse_var_decl()
        elif tok.type == TokenType.FUN:
            return self.parse_fun_decl()
        elif tok.type == TokenType.TEMPL:
            return self.parse_templ_decl()
        elif tok.type == TokenType.DATA:
            return self.parse_data_decl()
        elif tok.type == TokenType.INTERFACE:
            return self.parse_interface_decl()
        elif tok.type == TokenType.EXT:
            return self.parse_ext_decl()
        elif tok.type == TokenType.IF:
            return self.parse_if_stmt()
        elif tok.type == TokenType.WHILE:
            return self.parse_while_stmt()
        elif tok.type == TokenType.FOR:
            return self.parse_for_stmt()
        elif tok.type == TokenType.MATCH:
            return self.parse_match_stmt()
        elif tok.type == TokenType.RET:
            return self.parse_ret_stmt()
        elif tok.type == TokenType.BREAK:
            return self.parse_break_stmt()
        elif tok.type == TokenType.CONTINUE:
            return self.parse_continue_stmt()
        elif tok.type == TokenType.IMPORT:
            return self.parse_import_stmt()
        elif tok.type == TokenType.MODULE:
            return self.parse_module_stmt()
        else:
            return self.parse_expr_stmt()

    def parse_var_decl(self):
        kind = self.advance().type.name.lower()
        name = self.expect(TokenType.IDENT).value
        self.expect(TokenType.COLON)
        typ = self.parse_type()
        if self.peek().type == TokenType.ARROW:
            self.advance()
            val = self.parse_expr()
            return ('var_decl', kind, name, typ, val)
        return ('var_decl', kind, name, typ)

    def parse_fun_decl(self):
        self.advance()
        name = self.expect(TokenType.IDENT).value
        tparams = []
        if self.peek().type == TokenType.LT:
            self.advance()
            tparams = self.parse_type_param_list()
            self.expect(TokenType.GT)
        self.expect(TokenType.LPAREN)
        params = self.parse_param_list()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.COLON)
        rtype = self.parse_type()
        body = self.parse_body()
        self.expect(TokenType.END)
        return ('fun_decl', name, tparams, params, rtype, body)

    def parse_templ_decl(self):
        self.advance()
        name = self.expect(TokenType.IDENT).value
        tparams = []
        if self.peek().type == TokenType.LT:
            self.advance()
            tparams = self.parse_type_param_list()
            self.expect(TokenType.GT)
        fields = self.parse_field_list()
        self.expect(TokenType.END)
        return ('templ_decl', name, tparams, fields)

    def parse_data_decl(self):
        self.advance()
        name = self.expect(TokenType.IDENT).value
        tparams = []
        if self.peek().type == TokenType.LT:
            self.advance()
            tparams = self.parse_type_param_list()
            self.expect(TokenType.GT)
        fields = self.parse_field_list()
        self.expect(TokenType.END)
        return ('data_decl', name, tparams, fields)

    def parse_interface_decl(self):
        self.advance()
        name = self.expect(TokenType.IDENT).value
        sigs = self.parse_method_sig_list()
        self.expect(TokenType.END)
        return ('interface_decl', name, sigs)

    def parse_ext_decl(self):
        self.advance()
        type_expr = self.parse_type()
        self.expect(TokenType.DOT)
        name = self.expect(TokenType.IDENT).value
        self.expect(TokenType.LPAREN)
        params = self.parse_param_list()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.COLON)
        rtype = self.parse_type()
        body = self.parse_body()
        self.expect(TokenType.END)
        return ('ext_decl', type_expr, name, params, rtype, body)

    def parse_param_list(self):
        params = []
        self.skip_newlines()
        if self.peek().type != TokenType.RPAREN:
            params.append(self.parse_param())
            while True:
                self.skip_newlines()
                if self.peek().type != TokenType.COMMA:
                    break
                self.advance()
                params.append(self.parse_param())
        return params

    def parse_param(self):
        self.skip_newlines()
        name = self.expect(TokenType.IDENT).value
        self.expect(TokenType.COLON)
        typ = self.parse_type()
        if self.peek().type == TokenType.ARROW:
            self.advance()
            default = self.parse_expr()
            return ('param', name, typ, default)
        return ('param', name, typ)

    def parse_type_param_list(self):
        tparams = [self.expect(TokenType.IDENT).value]
        while self.peek().type == TokenType.COMMA:
            self.advance()
            tparams.append(self.expect(TokenType.IDENT).value)
        return tparams

    def parse_field_list(self):
        fields = []
        while True:
            self.skip_newlines()
            if self.peek().type != TokenType.IDENT:
                break
            name = self.advance().value
            self.expect(TokenType.COLON)
            typ = self.parse_type()
            fields.append(('field', name, typ))
        return fields

    def parse_method_sig_list(self):
        sigs = []
        while True:
            self.skip_newlines()
            if self.peek().type != TokenType.FUN:
                break
            self.advance()
            name = self.expect(TokenType.IDENT).value
            self.expect(TokenType.LPAREN)
            params = self.parse_param_list()
            self.expect(TokenType.RPAREN)
            self.expect(TokenType.COLON)
            rtype = self.parse_type()
            sigs.append(('method_sig', name, params, rtype))
        return sigs

    def parse_type(self):
        base = self.parse_base_type()
        if self.peek().type == TokenType.QUESTION:
            self.advance()
            return ('type', base, '?')
        elif self.peek().type == TokenType.LT:
            self.advance()
            targs = self.parse_type_list()
            self.expect(TokenType.GT)
            return ('type', base, *targs)
        return base

    def parse_type_list(self):
        types = [self.parse_type()]
        while self.peek().type == TokenType.COMMA:
            self.advance()
            types.append(self.parse_type())
        return types

    def parse_base_type(self):
        tok = self.peek()
        if tok.type in (TokenType.TYPE, TokenType.IDENT, TokenType.RESULT, TokenType.OK, TokenType.ERR, TokenType.NULL, TokenType.UNDEFINED):
            return self.advance().value
        raise SyntaxError(f"Expected type, got {tok.type.name}")

    def parse_body(self):
        stmts = []
        while True:
            self.skip_newlines()
            if self.peek().type in (TokenType.END, TokenType.EOF):
                break
            stmts.append(self.parse_stmt())
        return stmts

    def parse_if_stmt(self):
        self.advance()
        self.expect(TokenType.LPAREN)
        cond = self.parse_expr()
        self.expect(TokenType.RPAREN)
        then_body = self.parse_body()
        elseifs = []
        while True:
            self.skip_newlines()
            if self.peek().type != TokenType.ELSEIF:
                break
            self.advance()
            self.expect(TokenType.LPAREN)
            econd = self.parse_expr()
            self.expect(TokenType.RPAREN)
            ebody = self.parse_body()
            elseifs.append(('elseif', econd, ebody))
        else_body = []
        self.skip_newlines()
        if self.peek().type == TokenType.ELSE:
            self.advance()
            else_body = self.parse_body()
        self.expect(TokenType.END)
        return ('if_stmt', cond, then_body, elseifs, else_body)

    def parse_while_stmt(self):
        self.advance()
        self.expect(TokenType.LPAREN)
        cond = self.parse_expr()
        self.expect(TokenType.RPAREN)
        body = self.parse_body()
        self.expect(TokenType.END)
        return ('while_stmt', cond, body)

    def parse_for_stmt(self):
        self.advance()
        self.expect(TokenType.LPAREN)
        # Check for for-in: ident in expr
        saved_pos = self.pos
        if self.peek().type == TokenType.IDENT:
            test_tok = self.advance()
            if self.peek().type == TokenType.IDENT and self.peek().value == 'in':
                # It's for-in
                var_name = test_tok.value
                self.advance()  # consume 'in'
                iterable = self.parse_expr()
                self.expect(TokenType.RPAREN)
                body = self.parse_body()
                self.expect(TokenType.END)
                return ('for_in_stmt', var_name, iterable, body)
            # Not for-in, restore
            self.pos = saved_pos
        # C-style for
        init = self.parse_for_init()
        self.expect(TokenType.SEMICOLON)
        cond = self.parse_expr()
        self.expect(TokenType.SEMICOLON)
        step = self.parse_expr()
        self.expect(TokenType.RPAREN)
        body = self.parse_body()
        self.expect(TokenType.END)
        return ('for_stmt', init, cond, step, body)

    def parse_for_init(self):
        tok = self.peek()
        if tok.type == TokenType.IMM:
            self.advance()
            name = self.expect(TokenType.IDENT).value
            self.expect(TokenType.COLON)
            typ = self.parse_type()
            self.expect(TokenType.ARROW)
            val = self.parse_expr()
            return ('var_decl', 'imm', name, typ, val)
        elif tok.type == TokenType.NONIMM:
            self.advance()
            name = self.expect(TokenType.IDENT).value
            self.expect(TokenType.COLON)
            typ = self.parse_type()
            return ('var_decl', 'nonimm', name, typ)
        else:
            return self.parse_expr_stmt()

    def parse_match_stmt(self):
        self.advance()
        self.expect(TokenType.LPAREN)
        expr = self.parse_expr()
        self.expect(TokenType.RPAREN)
        arms = []
        while True:
            self.skip_newlines()
            if self.peek().type == TokenType.END:
                break
            arms.append(self.parse_match_arm())
        self.expect(TokenType.END)
        return ('match_stmt', expr, arms)

    def parse_match_arm(self):
        self.skip_newlines()
        pat = self.parse_pattern()
        self.expect(TokenType.ARROW)
        # Parse single statement/expression as arm body
        self.skip_newlines()
        body = [self.parse_stmt()]
        return ('match_arm', pat, body)

    def parse_pattern(self):
        self.skip_newlines()
        tok = self.peek()
        if tok.type == TokenType.IDENT:
            name = self.advance().value
            if name == '_':
                return ('pattern_wild',)
            if self.peek().type == TokenType.LPAREN:
                self.advance()
                pats = self.parse_pattern_list()
                self.expect(TokenType.RPAREN)
                return ('pattern_ctor', name, pats)
            return ('pattern_id', name)
        elif tok.type == TokenType.LBRACKET:
            self.advance()
            pats = self.parse_pattern_list()
            self.expect(TokenType.RBRACKET)
            return ('pattern_list', pats)
        elif tok.type in (TokenType.STRING, TokenType.NUMBER, TokenType.CHAR, TokenType.BOOLEAN, TokenType.HEX, TokenType.OCT, TokenType.BIN):
            return ('pattern_lit', self.parse_literal())
        else:
            raise SyntaxError(f"Unexpected pattern token: {tok.type.name}")

    def parse_pattern_list(self):
        pats = []
        self.skip_newlines()
        if self.peek().type not in (TokenType.RPAREN, TokenType.RBRACKET):
            pats.append(self.parse_pattern())
            while True:
                self.skip_newlines()
                if self.peek().type != TokenType.COMMA:
                    break
                self.advance()
                pats.append(self.parse_pattern())
        return pats

    def parse_ret_stmt(self):
        self.advance()
        self.skip_newlines()
        if self.peek().type in (TokenType.END, TokenType.EOF, TokenType.NEWLINE):
            return ('ret_stmt',)
        return ('ret_stmt', self.parse_expr())

    def parse_break_stmt(self):
        self.advance()
        return ('break_stmt',)

    def parse_continue_stmt(self):
        self.advance()
        return ('continue_stmt',)

    def parse_import_stmt(self):
        self.advance()
        path = self.expect(TokenType.STRING).value
        if self.peek().type == TokenType.AS:
            self.advance()
            name = self.expect(TokenType.IDENT).value
            return ('import_stmt', path, name)
        return ('import_stmt', path)

    def parse_module_stmt(self):
        self.advance()
        name = self.expect(TokenType.IDENT).value
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.IDENT)  # load
        self.expect(TokenType.LPAREN)
        path = self.expect(TokenType.STRING).value
        self.expect(TokenType.RPAREN)
        return ('module_stmt', name, path)

    def parse_expr_stmt(self):
        expr = self.parse_expr()
        return ('expr_stmt', expr)

    def parse_expr(self):
        return self.parse_assignment()

    def parse_assignment(self):
        left = self.parse_ternary()
        if self.peek().type == TokenType.ARROW:
            self.advance()
            return ('assign_expr', left, self.parse_expr())
        return left

    def parse_ternary(self):
        cond = self.parse_or()
        if self.peek().type == TokenType.QUESTION:
            self.advance()
            t = self.parse_expr()
            self.expect(TokenType.COLON)
            f = self.parse_expr()
            return ('ternary_expr', cond, t, f)
        elif self.peek().type == TokenType.ELVIS:
            self.advance()
            right = self.parse_ternary()
            return ('elvis_expr', cond, right)
        return cond

    def parse_or(self):
        return self.parse_left_assoc(self.parse_and, TokenType.OR)

    def parse_and(self):
        return self.parse_left_assoc(self.parse_bit_or, TokenType.AND)

    def parse_bit_or(self):
        return self.parse_left_assoc(self.parse_bit_xor, TokenType.BITOR)

    def parse_bit_xor(self):
        return self.parse_left_assoc(self.parse_bit_and, TokenType.BITXOR)

    def parse_bit_and(self):
        return self.parse_left_assoc(self.parse_equality, TokenType.BITAND)

    def parse_equality(self):
        return self.parse_left_assoc(self.parse_relational, TokenType.EQ, TokenType.NEQ)

    def parse_relational(self):
        return self.parse_left_assoc(self.parse_shift, TokenType.LT, TokenType.GT, TokenType.LE, TokenType.GE)

    def parse_shift(self):
        return self.parse_left_assoc(self.parse_additive, TokenType.LSHIFT, TokenType.RSHIFT)

    def parse_additive(self):
        return self.parse_left_assoc(self.parse_multiplicative, TokenType.PLUS, TokenType.MINUS)

    def parse_multiplicative(self):
        return self.parse_left_assoc(self.parse_power, TokenType.STAR, TokenType.SLASH, TokenType.PERCENT)

    def parse_power(self):
        base = self.parse_unary()
        if self.peek().type == TokenType.POWER:
            self.advance()
            return ('power_expr', base, self.parse_power())
        return base

    def parse_unary(self):
        tok = self.peek()
        if tok.type in (TokenType.NOT, TokenType.BANG):
            self.advance()
            return ('not_expr', self.parse_unary())
        elif tok.type == TokenType.BITNOT:
            self.advance()
            return ('bitnot_expr', self.parse_unary())
        elif tok.type == TokenType.MINUS:
            self.advance()
            return ('neg_expr', self.parse_unary())
        return self.parse_postfix()

    def parse_postfix(self):
        base = self.parse_primary()
        while True:
            tok = self.peek()
            if tok.type == TokenType.LPAREN:
                self.advance()
                args = self.parse_arg_list()
                self.expect(TokenType.RPAREN)
                base = ('call_expr', base, args)
            elif tok.type == TokenType.DOT:
                self.advance()
                field = self.expect(TokenType.IDENT).value
                base = ('field_expr', base, field)
            elif tok.type == TokenType.SAFE_ACCESS:
                self.advance()
                field = self.expect(TokenType.IDENT).value
                base = ('safe_field_expr', base, field)
            elif tok.type == TokenType.BANG:
                self.advance()
                base = ('unwrap_expr', base)
            elif tok.type == TokenType.LBRACKET:
                self.advance()
                idx = self.parse_expr()
                self.expect(TokenType.RBRACKET)
                base = ('index_expr', base, idx)
            else:
                break
        return base

    def parse_primary(self):
        tok = self.peek()
        if tok.type in (TokenType.NUMBER, TokenType.STRING, TokenType.CHAR, TokenType.BOOLEAN, TokenType.HEX, TokenType.OCT, TokenType.BIN):
            return ('literal', self.parse_literal())
        elif tok.type == TokenType.IDENT:
            return ('id_expr', self.advance().value)
        elif tok.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expr()
            self.expect(TokenType.RPAREN)
            return expr
        elif tok.type == TokenType.LBRACKET:
            self.advance()
            elems = self.parse_arg_list()
            self.expect(TokenType.RBRACKET)
            return ('list_expr', elems)
        elif tok.type == TokenType.LBRACE:
            self.advance()
            elems = self.parse_arg_list()
            self.expect(TokenType.RBRACE)
            return ('arr_expr', elems)
        elif tok.type == TokenType.LT:
            self.advance()
            pairs = self.parse_vect_pairs()
            self.expect(TokenType.GT)
            return ('vect_expr', pairs)
        elif tok.type == TokenType.OK:
            self.advance()
            self.expect(TokenType.LPAREN)
            val = self.parse_expr()
            self.expect(TokenType.RPAREN)
            return ('ok_expr', val)
        elif tok.type == TokenType.ERR:
            self.advance()
            self.expect(TokenType.LPAREN)
            val = self.parse_expr()
            self.expect(TokenType.RPAREN)
            return ('err_expr', val)
        elif tok.type == TokenType.NULL:
            self.advance()
            return ('literal', None)
        elif tok.type == TokenType.UNDEFINED:
            self.advance()
            return ('literal', None)
        elif tok.type == TokenType.LD:
            return self.parse_lambda()
        else:
            raise SyntaxError(f"Unexpected token in primary: {tok.type.name}")

    def parse_literal(self):
        tok = self.advance()
        if tok.type == TokenType.HEX:
            return int(tok.value[2:], 16)
        elif tok.type == TokenType.OCT:
            return int(tok.value[2:], 8)
        elif tok.type == TokenType.BIN:
            return int(tok.value[2:], 2)
        return tok.value

    def parse_arg_list(self):
        args = []
        self.skip_newlines()
        if self.peek().type not in (TokenType.RPAREN, TokenType.RBRACKET, TokenType.RBRACE):
            args.append(self.parse_expr())
            while True:
                self.skip_newlines()
                if self.peek().type != TokenType.COMMA:
                    break
                self.advance()
                args.append(self.parse_expr())
        return args

    def parse_vect_pairs(self):
        pairs = []
        while True:
            self.skip_newlines()
            if self.peek().type != TokenType.LT:
                break
            self.advance()
            x = self.parse_expr()
            self.expect(TokenType.COMMA)
            y = self.parse_expr()
            self.expect(TokenType.GT)
            pairs.append(('vect_pair', x, y))
        return pairs

    def parse_lambda(self):
        self.advance()
        name = None
        if self.peek().type == TokenType.IDENT:
            name = self.advance().value
        self.expect(TokenType.LPAREN)
        params = self.parse_param_list()
        self.expect(TokenType.RPAREN)
        body = self.parse_body()
        self.expect(TokenType.END)
        return ('lambda_expr', name, params, body)

    def parse_left_assoc(self, parse_next, *op_types):
        left = parse_next()
        while self.peek().type in op_types:
            op = self.advance().type
            right = parse_next()
            left = ('bin_expr', op, left, right)
        return left

# ============================================================
# SECTION 10: INTERPRETER
# ============================================================

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class BreakLoop(Exception):
    pass

class ContinueLoop(Exception):
    pass

class SolEnv:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent
        self.types = {}

    def define(self, name, value, typ=None):
        self.vars[name] = value
        if typ:
            self.types[name] = typ

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        if self.parent:
            return self.parent.get(name)
        raise NameError(f"Undefined variable: {name}")

    def set(self, name, value):
        if name in self.vars:
            self.vars[name] = value
            return
        if self.parent:
            self.parent.set(name, value)
            return
        raise NameError(f"Undefined variable: {name}")

class Interpreter:
    def __init__(self):
        self.globals = SolEnv()
        self.env = self.globals
        self.functions = {}
        self.structs = {}
        self._setup_builtins()

    def _type_check(self, value, typ):
        if typ is None or typ == 'any':
            return True
        base = typ[1] if isinstance(typ, tuple) and typ[0] == 'type' else typ
        if base in ('integer', 'int16', 'int32', 'int64'):
            return isinstance(value, int) and not isinstance(value, bool)
        elif base in ('float', 'float32', 'float64'):
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        elif base == 'boolean':
            return isinstance(value, bool)
        elif base == 'string':
            return isinstance(value, str)
        elif base == 'char':
            return isinstance(value, str) and len(value) == 1
        elif base == 'list':
            return isinstance(value, list)
        elif base == 'arr':
            return isinstance(value, list)
        elif base == 'map':
            return isinstance(value, dict) and '__type__' not in value
        elif base == 'vect':
            return isinstance(value, SolVect)
        elif base == 'Result':
            return isinstance(value, (Ok, Err))
        elif base in ('null', 'nothing', 'undefined'):
            return value is None
        elif base in self.structs:
            return isinstance(value, dict) and value.get('__type__') == base
        return True

    def _setup_builtins(self):
        # I/O
        self.globals.define('std.out', std_out)
        self.globals.define('std.outln', std_outln)
        self.globals.define('std.in', std_in)
        self.globals.define('std.err', std_err)
        self.globals.define('std.quit', std_quit)
        self.globals.define('std.load', std_load)
        self.globals.define('std.save', std_save)
        self.globals.define('std.lasterr', std_lasterr)
        self.globals.define('std.clearerr', std_clearerr)
        # String
        self.globals.define('string.upper', string_upper)
        self.globals.define('string.lower', string_lower)
        self.globals.define('string.has', string_has)
        self.globals.define('string.nothave', string_nothave)
        self.globals.define('string.length', string_length)
        self.globals.define('string.isempty', string_isempty)
        self.globals.define('string.isnumeric', string_isnumeric)
        self.globals.define('string.isalpha', string_isalpha)
        self.globals.define('string.isalphanum', string_isalphanum)
        self.globals.define('string.titlecase', string_titlecase)
        self.globals.define('string.camelcase', string_camelcase)
        self.globals.define('string.snakecase', string_snakecase)
        self.globals.define('string.kebabcase', string_kebabcase)
        self.globals.define('string.trim', string_trim)
        self.globals.define('string.trimleft', string_trimleft)
        self.globals.define('string.trimright', string_trimright)
        # Type conversions
        self.globals.define('type.toString', type_toString)
        self.globals.define('type.strToInteger', type_strToInteger)
        self.globals.define('type.flToInt', type_flToInt)
        self.globals.define('type.iToFloat', type_iToFloat)
        self.globals.define('type.iToHex', type_iToHex)
        self.globals.define('type.iToOct', type_iToOct)
        self.globals.define('type.octToInt', type_octToInt)
        self.globals.define('type.hexToInt', type_hexToInt)
        self.globals.define('type.binaryToInt', type_binaryToInt)
        self.globals.define('type.boolToInt', type_boolToInt)
        self.globals.define('type.intToBool', type_intToBool)
        # List
        self.globals.define('list.push', list_push)
        self.globals.define('list.pop', list_pop)
        self.globals.define('list.insert', list_insert)
        self.globals.define('list.remove', list_remove)
        self.globals.define('list.removeval', list_removeval)
        self.globals.define('list.find', list_find)
        self.globals.define('list.sort', list_sort)
        self.globals.define('list.reverse', list_reverse)
        self.globals.define('list.clear', list_clear)
        self.globals.define('list.len', list_len)
        self.globals.define('list.copy', list_copy)
        self.globals.define('list.slice', list_slice)
        self.globals.define('list.first', list_first)
        self.globals.define('list.last', list_last)
        self.globals.define('list.contains', list_contains)
        # Map
        self.globals.define('map.set', map_set)
        self.globals.define('map.get', map_get)
        self.globals.define('map.remove', map_remove)
        self.globals.define('map.has', map_has)
        self.globals.define('map.keys', map_keys)
        self.globals.define('map.values', map_values)
        self.globals.define('map.len', map_len)
        self.globals.define('map.clear', map_clear)
        self.globals.define('map.contains', map_contains)
        # Result
        self.globals.define('Ok', lambda v: Ok(v))
        self.globals.define('Err', lambda m: Err(m))
        self.globals.define('result.isOk', result_isOk)
        self.globals.define('result.isErr', result_isErr)
        self.globals.define('result.unwrap', result_unwrap)
        self.globals.define('result.unwrapOr', result_unwrapOr)
        self.globals.define('result.unwrapOrElse', result_unwrapOrElse)
        self.globals.define('result.expect', result_expect)
        self.globals.define('result.map', result_map)
        self.globals.define('result.mapErr', result_mapErr)
        self.globals.define('result.andThen', result_andThen)
        self.globals.define('nothing', None)

    def run(self, ast):
        _, stmts = ast
        for stmt in stmts:
            self.eval_stmt(stmt)

    def eval_stmt(self, stmt):
        tag = stmt[0]
        if tag == 'var_decl':
            _, kind, name, typ, *rest = stmt
            if rest:
                val = self.eval_expr(rest[0])
            else:
                base = typ[1] if isinstance(typ, tuple) and typ[0] == 'type' else typ
                if base in ('integer', 'int16', 'int32', 'int64', 'float', 'float32', 'float64'):
                    val = 0
                elif base == 'boolean':
                    val = False
                elif base == 'string':
                    val = ""
                elif base == 'char':
                    val = '\0'
                elif base in ('list', 'arr'):
                    val = []
                elif base == 'map':
                    val = {}
                elif base == 'vect':
                    val = SolVect([])
                else:
                    val = None
            if typ and not self._type_check(val, typ):
                raise TypeError(f"Type mismatch: expected {typ}, got {type(val).__name__} for variable '{name}'")
            self.env.define(name, val, typ)
        elif tag == 'fun_decl':
            _, name, tparams, params, rtype, body = stmt
            self.functions[name] = (params, rtype, body, self.env)
        elif tag == 'templ_decl':
            _, name, tparams, *fields = stmt
            self.structs[name] = ('templ', fields)
            field_names = [f[1] for f in fields]
            def make_templ(*args):
                obj = {}
                for i, fn in enumerate(field_names):
                    obj[fn] = args[i] if i < len(args) else None
                obj['__type__'] = name
                return obj
            self.globals.define(name, make_templ)
        elif tag == 'data_decl':
            _, name, tparams, *fields = stmt
            self.structs[name] = ('data', fields)
            field_names = [f[1] for f in fields]
            def make_data(*args):
                obj = {}
                for i, fn in enumerate(field_names):
                    obj[fn] = args[i] if i < len(args) else None
                obj['__type__'] = name
                obj['__immutable__'] = True
                return obj
            self.globals.define(name, make_data)
        elif tag == 'interface_decl':
            _, name, *sigs = stmt
            self.structs[name] = ('interface', sigs)
        elif tag == 'ext_decl':
            _, type_expr, name, params, rtype, body = stmt
            ext_key = f"{type_expr[1] if isinstance(type_expr, tuple) else type_expr}.{name}"
            self.functions[ext_key] = (params, rtype, body, self.env)
        elif tag == 'if_stmt':
            _, cond, then_body, elseifs, else_body = stmt
            if self.eval_expr(cond):
                for s in then_body:
                    self.eval_stmt(s)
            else:
                matched = False
                for econd, ebody in elseifs:
                    if self.eval_expr(econd):
                        for s in ebody:
                            self.eval_stmt(s)
                        matched = True
                        break
                if not matched:
                    for s in else_body:
                        self.eval_stmt(s)
        elif tag == 'while_stmt':
            _, cond, body = stmt
            while True:
                if not self.eval_expr(cond):
                    break
                try:
                    for s in body:
                        self.eval_stmt(s)
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
        elif tag == 'for_stmt':
            _, init, cond, step, body = stmt
            self.eval_stmt(init)
            while True:
                if not self.eval_expr(cond):
                    break
                try:
                    for s in body:
                        self.eval_stmt(s)
                except BreakLoop:
                    break
                except ContinueLoop:
                    pass
                self.eval_expr(step)
        elif tag == 'for_in_stmt':
            _, var_name, iterable, body = stmt
            items = self.eval_expr(iterable)
            for item in items:
                self.env.define(var_name, item)
                try:
                    for s in body:
                        self.eval_stmt(s)
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
        elif tag == 'match_stmt':
            _, expr, arms = stmt
            val = self.eval_expr(expr)
            for arm in arms:
                _, pat, body = arm
                if self._match_pattern(pat, val):
                    for s in body:
                        self.eval_stmt(s)
                    break
            else:
                raise RuntimeError("Non-exhaustive match")
        elif tag == 'ret_stmt':
            if len(stmt) == 1:
                raise ReturnValue(None)
            raise ReturnValue(self.eval_expr(stmt[1]))
        elif tag == 'break_stmt':
            raise BreakLoop()
        elif tag == 'continue_stmt':
            raise ContinueLoop()
        elif tag == 'expr_stmt':
            return self.eval_expr(stmt[1])
        elif tag == 'import_stmt':
            _, path, *rest = stmt
            import_path = path.strip('"')
            if not os.path.isabs(import_path):
                import_path = os.path.join(os.getcwd(), import_path)
            if not import_path.endswith('.sol'):
                import_path += '.sol'
            if os.path.exists(import_path):
                with open(import_path, 'r') as f:
                    source = f.read()
                lexer = Lexer(source)
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                ast = parser.parse()
                module_interpreter = Interpreter()
                module_interpreter.run(ast)
                if rest:
                    alias = rest[0]
                    self.env.define(alias, module_interpreter.globals.vars)
                else:
                    for k, v in module_interpreter.globals.vars.items():
                        self.env.define(k, v)
            else:
                raise RuntimeError(f"Module not found: {import_path}")
        elif tag == 'module_stmt':
            _, name, path = stmt
            import_path = path.strip('"')
            if not os.path.isabs(import_path):
                import_path = os.path.join(os.getcwd(), import_path)
            if not import_path.endswith('.sol'):
                import_path += '.sol'
            if os.path.exists(import_path):
                with open(import_path, 'r') as f:
                    source = f.read()
                lexer = Lexer(source)
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                ast = parser.parse()
                module_interpreter = Interpreter()
                module_interpreter.run(ast)
                self.env.define(name, module_interpreter.globals.vars)
            else:
                raise RuntimeError(f"Module not found: {import_path}")
        else:
            raise RuntimeError(f"Unknown statement: {tag}")

    def _match_pattern(self, pat, val):
        tag = pat[0]
        if tag == 'pattern_wild':
            return True
        elif tag == 'pattern_id':
            self.env.define(pat[1], val)
            return True
        elif tag == 'pattern_lit':
            return pat[1] == val
        elif tag == 'pattern_list':
            if not isinstance(val, list):
                return False
            pats = pat[1]
            if len(pats) != len(val):
                return False
            for p, v in zip(pats, val):
                if not self._match_pattern(p, v):
                    return False
            return True
        elif tag == 'pattern_ctor':
            if not isinstance(val, dict) or val.get('__type__') != pat[1]:
                return False
            pats = pat[2]
            struct_info = self.structs.get(pat[1])
            if not struct_info:
                return False
            fields = [f[1] for f in struct_info[1]]
            if len(pats) != len(fields):
                return False
            for p, fname in zip(pats, fields):
                if not self._match_pattern(p, val.get(fname)):
                    return False
            return True
        return False

    def eval_expr(self, expr):
        if not isinstance(expr, tuple):
            return expr
        tag = expr[0]
        if tag == 'literal':
            return expr[1]
        elif tag == 'id_expr':
            return self.env.get(expr[1])
        elif tag == 'assign_expr':
            target = expr[1]
            val = self.eval_expr(expr[2])
            if target[0] == 'id_expr':
                self.env.set(target[1], val)
            elif target[0] == 'field_expr':
                obj = self.eval_expr(target[1])
                field = target[2]
                if isinstance(obj, dict):
                    obj[field] = val
                else:
                    setattr(obj, field, val)
            elif target[0] == 'index_expr':
                obj = self.eval_expr(target[1])
                idx = self.eval_expr(target[2])
                obj[idx] = val
            return val
        elif tag == 'ternary_expr':
            _, cond, t, f = expr
            return self.eval_expr(t) if self.eval_expr(cond) else self.eval_expr(f)
        elif tag == 'elvis_expr':
            _, left, right = expr
            val = self.eval_expr(left)
            return val if val is not None else self.eval_expr(right)
        elif tag == 'bin_expr':
            _, op, left, right = expr
            lv = self.eval_expr(left)
            rv = self.eval_expr(right)
            return self._binop(op, lv, rv)
        elif tag == 'not_expr':
            return not self.eval_expr(expr[1])
        elif tag == 'bitnot_expr':
            return ~self.eval_expr(expr[1])
        elif tag == 'neg_expr':
            return -self.eval_expr(expr[1])
        elif tag == 'call_expr':
            func_expr = expr[1]
            args = [self.eval_expr(a) for a in expr[2]]
            if func_expr[0] == 'id_expr':
                fname = func_expr[1]
                if fname in self.functions:
                    params, rtype, body, closure = self.functions[fname]
                    new_env = SolEnv(closure)
                    for p, arg in zip(params, args):
                        pname = p[1]
                        ptype = p[2] if len(p) > 2 else None
                        if ptype and not self._type_check(arg, ptype):
                            raise TypeError(f"Type mismatch in argument '{pname}': expected {ptype}, got {type(arg).__name__}")
                        new_env.define(pname, arg, ptype)
                    old_env = self.env
                    self.env = new_env
                    try:
                        for s in body:
                            self.eval_stmt(s)
                        result = None
                    except ReturnValue as rv:
                        result = rv.value
                    finally:
                        self.env = old_env
                    if rtype and not self._type_check(result, rtype):
                        raise TypeError(f"Return type mismatch: expected {rtype}, got {type(result).__name__}")
                    return result
                else:
                    fn = self.env.get(fname)
                    return fn(*args)
            else:
                fn = self.eval_expr(func_expr)
                return fn(*args)
        elif tag == 'field_expr':
            obj_expr = expr[1]
            field = expr[2]
            if obj_expr[0] == 'id_expr':
                full_name = obj_expr[1] + '.' + field
                try:
                    return self.env.get(full_name)
                except NameError:
                    pass
                ext_key = f"{obj_expr[1]}.{field}"
                if ext_key in self.functions:
                    params, rtype, body, closure = self.functions[ext_key]
                    def bound_method(*args):
                        obj_val = self.env.get(obj_expr[1])
                        new_env = SolEnv(closure)
                        if params:
                            new_env.define(params[0][1], obj_val)
                        for p, arg in zip(params[1:], args):
                            pname = p[1]
                            new_env.define(pname, arg)
                        old_env = self.env
                        self.env = new_env
                        try:
                            for s in body:
                                self.eval_stmt(s)
                            return None
                        except ReturnValue as rv:
                            return rv.value
                        finally:
                            self.env = old_env
                    return bound_method
            obj = self.eval_expr(obj_expr)
            if isinstance(obj, dict):
                return obj.get(field)
            if hasattr(obj, field):
                return getattr(obj, field)
            raise AttributeError(f"No field {field} on {type(obj)}")
        elif tag == 'safe_field_expr':
            obj = self.eval_expr(expr[1])
            if obj is None:
                return None
            field = expr[2]
            if isinstance(obj, dict):
                return obj.get(field)
            if hasattr(obj, field):
                return getattr(obj, field)
            return None
        elif tag == 'unwrap_expr':
            val = self.eval_expr(expr[1])
            if val is None:
                raise RuntimeError("Force unwrap of null")
            return val
        elif tag == 'index_expr':
            obj = self.eval_expr(expr[1])
            idx = self.eval_expr(expr[2])
            return obj[idx]
        elif tag == 'list_expr':
            return [self.eval_expr(e) for e in expr[1]]
        elif tag == 'arr_expr':
            return [self.eval_expr(e) for e in expr[1]]
        elif tag == 'vect_expr':
            pairs = []
            for p in expr[1]:
                _, x, y = p
                pairs.append((self.eval_expr(x), self.eval_expr(y)))
            return SolVect(pairs)
        elif tag == 'ok_expr':
            return Ok(self.eval_expr(expr[1]))
        elif tag == 'err_expr':
            return Err(self.eval_expr(expr[1]))
        elif tag == 'lambda_expr':
            _, name, params, body = expr
            captured_env = self.env
            def lambda_fn(*args):
                new_env = SolEnv(captured_env)
                for p, arg in zip(params, args):
                    pname = p[1]
                    new_env.define(pname, arg)
                old_env = self.env
                self.env = new_env
                try:
                    for s in body:
                        self.eval_stmt(s)
                    return None
                except ReturnValue as rv:
                    return rv.value
                finally:
                    self.env = old_env
            return lambda_fn
        elif tag == 'power_expr':
            return self.eval_expr(expr[1]) ** self.eval_expr(expr[2])
        else:
            raise RuntimeError(f"Unknown expression: {tag}")

    def _binop(self, op, l, r):
        ops = {
            TokenType.PLUS: lambda a, b: a + b,
            TokenType.MINUS: lambda a, b: a - b,
            TokenType.STAR: lambda a, b: a * b,
            TokenType.SLASH: lambda a, b: a / b,
            TokenType.PERCENT: lambda a, b: a % b,
            TokenType.POWER: lambda a, b: a ** b,
            TokenType.EQ: lambda a, b: a == b,
            TokenType.NEQ: lambda a, b: a != b,
            TokenType.LT: lambda a, b: a < b,
            TokenType.GT: lambda a, b: a > b,
            TokenType.LE: lambda a, b: a <= b,
            TokenType.GE: lambda a, b: a >= b,
            TokenType.AND: lambda a, b: a and b,
            TokenType.OR: lambda a, b: a or b,
            TokenType.BITAND: lambda a, b: a & b,
            TokenType.BITOR: lambda a, b: a | b,
            TokenType.BITXOR: lambda a, b: a ^ b,
            TokenType.LSHIFT: lambda a, b: a << b,
            TokenType.RSHIFT: lambda a, b: a >> b,
        }
        if op in ops:
            return ops[op](l, r)
        raise RuntimeError(f"Unknown operator: {op}")

# ============================================================
# SECTION 11: CLI
# ============================================================

def run_file(path):
    with open(path, 'r') as f:
        source = f.read()
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.run(ast)

def run_repl():
    print("SOL Interpreter v0.1.0")
    print("Type 'quit' to exit")
    interpreter = Interpreter()
    while True:
        try:
            line = input("sol> ")
            if line.strip() == 'quit':
                break
            lexer = Lexer(line)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            interpreter.run(ast)
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_repl()
