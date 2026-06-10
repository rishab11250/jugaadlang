"""
faili — JugaadLang File System Operations Module.
"""

import os
import shutil


def padho(path: str) -> str:
    """Read full file contents."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def likho(path: str, content: str) -> None:
    """Write text to a file (overwrites existing contents)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def jodo(path: str, content: str) -> None:
    """Append text to a file."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def mitao(path: str) -> None:
    """Delete a file or directory."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def hai_kya(path: str) -> bool:
    """Check if file or directory exists."""
    return os.path.exists(path)


def list_karo(path: str = ".") -> list[str]:
    """List directory contents."""
    return os.listdir(path)


def folder_banao(path: str) -> None:
    """Create directory and parents if they don't exist."""
    os.makedirs(path, exist_ok=True)
