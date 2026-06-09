"""
JugaadLang Errors — Humorous Hindi error messages for developers.
"""
from __future__ import annotations
import traceback
import sys
import re
from typing import Optional, Any
from rich.console import Console
from rich.panel import Panel

# Custom Exception Classes
class JugaadError(Exception):
    """Base class for all JugaadLang compiler and runtime errors."""
    def __init__(self, message: str, line: Optional[int] = None, col: Optional[int] = None):
        super().__init__(message)
        self.line = line
        self.col = col


class JugaadSyntaxError(JugaadError):
    """Syntax error (🤦 Bhai kya likh diya?)."""
    pass


class JugaadRuntimeError(JugaadError):
    """General runtime error."""
    pass


class JugaadNameError(JugaadRuntimeError):
    """Variable not found (🕵️ Variable dhundte dhundte thak gaya)."""
    pass


class JugaadTypeError(JugaadRuntimeError):
    """Type mismatch (🤔 Type mismatch ho gaya)."""
    pass


class JugaadZeroDivisionError(JugaadRuntimeError):
    """Zero division (💀 Zero se divide?)."""
    pass


FUNNY_ERRORS = {
    "SyntaxError": {
        "title": "🤦 Bhai kya likh diya?",
        "body": "Keyboard strike par hai kya? Code check karo.",
    },
    "NameError": {
        "title": "🕵️ Variable dhundte dhundte thak gaya.",
        "body": "Possible reasons:\n  • Typo kiya hai\n  • Variable declare karna bhool gaye\n  • Universe collapse ho gaya",
    },
    "ZeroDivisionError": {
        "title": "💀 Zero se divide?",
        "body": "Newton bhi confuse ho gaya. Maths seekh lo thoda.",
    },
    "TypeError": {
        "title": "🤔 Type mismatch ho gaya.",
        "body": "Galat data-type use kiya hai. Computation shock me chala gaya.",
    },
    "IndexError": {
        "title": "🎯 Index out of bounds!",
        "body": "List ke bahar chala gaya! Itna bada index kahan se mila?",
    },
    "KeyError": {
        "title": "🔑 Key gayab hai!",
        "body": "Dictionary mein ye key to hai hi nahi. Dhyan se check karo.",
    },
    "AttributeError": {
        "title": "🚫 Attribute mila hi nahi.",
        "body": "Object me ye feature/method nahi hai boss.",
    },
    "ModuleNotFoundError": {
        "title": "📦 Module missing!",
        "body": "Dhundne se bhi nahi mila. Install kiya hai kya? (jug install check karo)",
    },
}


def format_syntax_error(msg: str, line: int, col: int, source_line: str, filename: str = "<stdin>") -> str:
    """Format syntax errors nicely with caret highlighting and funny title."""
    console = Console(color_system="truecolor", force_terminal=True)
    with console.capture() as capture:
        console.print(f"[bold red]🤦 Bhai kya likh diya?[/bold red]")
        console.print(f"[yellow]Faili:[/yellow] [cyan]{filename}[/cyan] [yellow]Line {line}, Col {col}[/yellow]\n")
        
        if source_line:
            # Clean and display source line
            clean_line = source_line.rstrip()
            console.print(f"  {clean_line}")
            # Align caret
            caret_spaces = " " * (col + 1)
            console.print(f"  {caret_spaces}[bold red]^[/bold red]")
            
        console.print(f"\n[bold white]Error Details:[/bold white] {msg}")
        console.print("[dim]Keyboard strike par hai kya?[/dim]")
    return capture.get()


def extract_original_line_no(exc: Exception) -> Optional[int]:
    """Helper to extract line number from execution traceback."""
    tb = exc.__traceback__
    last_line = None
    while tb:
        # We look for files loaded in compiler/runtime.
        # Usually compiled using exec() and has filename "<string>" or matching the user file.
        filename = tb.tb_frame.f_code.co_filename
        if filename != __file__:
            last_line = tb.tb_lineno
        tb = tb.tb_next
    return last_line


def format_error(exc: Exception, source: str = "", filename: str = "<stdin>") -> str:
    """
    Format standard Python exception into a premium, humorous JugaadLang message.
    """
    exc_type_name = type(exc).__name__
    
    # Check if we have a custom handler
    info = FUNNY_ERRORS.get(exc_type_name, {
        "title": f"💥 Gadbad Ho Gayi ({exc_type_name})",
        "body": str(exc)
    })
    
    # Try to find line number
    line_no = None
    if hasattr(exc, "line") and exc.line is not None:
        line_no = exc.line
    elif isinstance(exc, SyntaxError):
        line_no = exc.lineno
    else:
        line_no = extract_original_line_no(exc)
        
    col_no = getattr(exc, "col", 1)
    if isinstance(exc, SyntaxError) and exc.offset is not None:
        col_no = exc.offset
        
    source_lines = source.splitlines() if source else []
    source_line = ""
    if line_no and 0 < line_no <= len(source_lines):
        source_line = source_lines[line_no - 1]
        
    # Standard formatters
    if exc_type_name == "SyntaxError" or isinstance(exc, JugaadSyntaxError):
        # Extract syntax error message
        err_msg = str(exc)
        if isinstance(exc, SyntaxError):
            err_msg = exc.msg or ""
        return format_syntax_error(err_msg, line_no or 1, col_no, source_line, filename)
        
    # For runtime errors
    console = Console(color_system="truecolor", force_terminal=True)
    with console.capture() as capture:
        title = info["title"]
        body = info["body"]
        
        # NameError specific extraction (extract variable name)
        if exc_type_name == "NameError":
            match = re.search(r"name '(\w+)' is not defined", str(exc))
            var_name = match.group(1) if match else "variable"
            title = f"🕵️ Variable '{var_name}' dhundte dhundte thak gaya."
            body = f"'{var_name}' mila hi nahi.\n\n" + info["body"]
            
        console.print(f"[bold red]{title}[/bold red]")
        if line_no:
            console.print(f"[yellow]Faili:[/yellow] [cyan]{filename}[/cyan] [yellow]Line {line_no}[/yellow]\n")
            if source_line:
                console.print(f"  [dim]>[/dim] {source_line.strip()}")
        else:
            console.print(f"[yellow]Faili:[/yellow] [cyan]{filename}[/cyan]\n")
            
        console.print(f"\n[bold white]Kya gadbad hai?[/bold white]")
        # Output traceback details if in debug mode or for extra detail
        # Show clean error explanation
        console.print(f"  {body}")
        
        # ZeroDivisionError, TypeError, KeyError etc might need original error message too
        if exc_type_name not in ("NameError", "SyntaxError"):
            console.print(f"\n[dim]Original System Error: {exc}[/dim]")
            
    return capture.get()
