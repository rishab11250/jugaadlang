# jugaadlang/errors/__init__.py
from .messages import (
    format_error,
    format_syntax_error,
    JugaadError,
    JugaadSyntaxError,
    JugaadRuntimeError,
    JugaadNameError,
    JugaadTypeError,
    JugaadZeroDivisionError,
    FUNNY_ERRORS,
)

__all__ = [
    "format_error",
    "format_syntax_error",
    "JugaadError",
    "JugaadSyntaxError",
    "JugaadRuntimeError",
    "JugaadNameError",
    "JugaadTypeError",
    "JugaadZeroDivisionError",
    "FUNNY_ERRORS",
]
