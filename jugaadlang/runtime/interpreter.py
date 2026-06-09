"""
JugaadLang Runtime — Executes JugaadLang AST after transpiling to Python.
"""
from __future__ import annotations
import ast
import sys
import os
import random
from typing import Any

from ..lexer.lexer import Lexer
from ..parser.parser import Parser
from ..parser.parser import ParseError
from ..transformer.to_python import JugaadToPythonTransformer
from ..ast_nodes.nodes import ExprStmt
from ..errors.messages import format_error, JugaadError


# ── Built-in functions ────────────────────────────────────────────────────────

def chai() -> None:
    """Print a funny message about Chai."""
    print("☕ Chai pi lo. (Chai is life!)")


def himmat() -> None:
    """Print a hidden feature message."""
    print("🔥 Hidden feature detected. Aapke andar himmat hai!")


def ghaas_chhoo() -> None:
    """Print a touch grass message."""
    print("🌱 Bahar ghoom aao. Go touch some grass!")


def bachao() -> None:
    """Print a stackoverflow search message."""
    print("🚨 StackOverflow search shuru. Bachao bachao!")


def fortune() -> None:
    """Print a random funny fortune."""
    fortunes = [
        "🔮 Bug line 347 mein ho sakta hai.",
        "🔮 Agla deploy Friday ko mat karna.",
        "🔮 Error resolved ho chuka hai, bas code likhna baaki hai.",
        "🔮 Shani bhaari hai aapke variable declarations par.",
        "🔮 Chai cup mein garam hai, compiler keyboard par ready hai.",
    ]
    print(random.choice(fortunes))


def jugaad_help() -> None:
    """Print standard jugaad tips."""
    tips = [
        "🛠️ Restart karke dekho, 90% bugs solve ho jaate hain.",
        "🛠️ Print statement dalkar debug karo, debugger to shauk ke liye hai.",
        "🛠️ Commit karke so jao, subah tak apne aap thik ho jayega.",
        "🛠️ StackOverflow se copy karte waqt variable name change karna na bhoolna.",
    ]
    print(random.choice(tips))


# ── Interpreter ───────────────────────────────────────────────────────────────

class JugaadInterpreter:
    """
    Executes JugaadLang code.
    Maintains a persistent global execution context, ideal for REPL session reuse.
    """

    def __init__(self, filename: str = "<stdin>") -> None:
        self.filename = filename
        
        # Persistent global namespace
        self.globals: dict[str, Any] = {
            "__builtins__": __builtins__,
            # Built-in variables
            "bolo": print,
            "poochho": input,
            # Built-in funny functions
            "chai": chai,
            "himmat": himmat,
            "ghaas_chhoo": ghaas_chhoo,
            "bachao": bachao,
            "fortune": fortune,
            "jugaad": jugaad_help,
        }

        # Set up stdlib import path
        stdlib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stdlib"))
        if stdlib_path not in sys.path:
            sys.path.insert(0, stdlib_path)

    def run(self, source: str) -> None:
        """Run JugaadLang source code as statements (exec mode)."""
        try:
            # 1. Lexical analysis
            lexer = Lexer(source, self.filename)
            tokens = lexer.tokenize()
            
            # 2. Syntax analysis
            parser = Parser(tokens, self.filename, source)
            ast_mod = parser.parse()
            
            # 3. Transpile to Python AST
            transformer = JugaadToPythonTransformer(self.filename)
            py_ast = transformer.transform(ast_mod)
            
            # 4. Compile Python AST to bytecode
            code_obj = compile(py_ast, self.filename, "exec")
            
            # 5. Execute bytecode in the persistent namespace
            exec(code_obj, self.globals, self.globals)
        except Exception as e:
            # Print funny error message and re-raise / handle
            formatted = format_error(e, source, self.filename)
            print(formatted, file=sys.stderr)
            raise

    def run_expression(self, source: str) -> Any:
        """
        Evaluate JugaadLang source.
        If it's a single expression, evaluate and return its value (eval mode).
        Otherwise, execute as standard statements (exec mode).
        """
        try:
            lexer = Lexer(source, self.filename)
            tokens = lexer.tokenize()
            parser = Parser(tokens, self.filename, source)
            ast_mod = parser.parse()
            
            # If the source is a single expression statement, evaluate it and return the result
            if len(ast_mod.body) == 1 and isinstance(ast_mod.body[0], ExprStmt):
                expr_node = ast_mod.body[0].value
                
                transformer = JugaadToPythonTransformer(self.filename)
                py_expr_ast = transformer.visit(expr_node)
                
                py_expr = ast.Expression(body=py_expr_ast)
                ast.fix_missing_locations(py_expr)
                
                code_obj = compile(py_expr, self.filename, "eval")
                return eval(code_obj, self.globals, self.globals)
            else:
                # Compile and execute as a normal module block
                transformer = JugaadToPythonTransformer(self.filename)
                py_ast = transformer.transform(ast_mod)
                code_obj = compile(py_ast, self.filename, "exec")
                exec(code_obj, self.globals, self.globals)
                return None
        except Exception as e:
            formatted = format_error(e, source, self.filename)
            print(formatted, file=sys.stderr)
            raise
