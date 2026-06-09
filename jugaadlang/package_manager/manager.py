"""
JugaadPackageManager — Standard package manager for JugaadLang.
Wraps pip and manages custom package maps (e.g. 'web' installing flask/requests).
"""
from __future__ import annotations
import sys
import subprocess
import requests
from typing import Any
from rich.console import Console
from rich.table import Table

console = Console(color_system="truecolor", force_terminal=True)

# Custom package mappings for JugaadLang ecosystem
PACKAGE_MAP = {
    "web": ["flask", "requests", "httpx", "aiohttp"],
    "dev": ["pytest", "pytest-cov", "black", "mypy", "ruff"],
    "ml": ["numpy", "pandas", "scikit-learn", "matplotlib"],
}


class JugaadPackageManager:
    """
    Manages package installation, removal, update, and search for JugaadLang.
    """

    @staticmethod
    def install(package: str) -> None:
        """Install a package or custom bundle."""
        targets = PACKAGE_MAP.get(package, [package])
        
        console.print(f"[bold green]📦 JugaadLang Package Manager[/bold green]")
        console.print(f"Installing [cyan]{package}[/cyan]...")
        
        try:
            cmd = [sys.executable, "-m", "pip", "install"] + targets
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            console.print(f"[bold green]✓ Success![/bold green] Installed {package} successfully.")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]✗ Error: Installation fail ho gayi![/bold red]")
            console.print(f"[dim]{e.stderr}[/dim]")

    @staticmethod
    def remove(package: str) -> None:
        """Uninstall a package."""
        targets = PACKAGE_MAP.get(package, [package])
        
        console.print(f"[bold green]📦 JugaadLang Package Manager[/bold green]")
        console.print(f"Removing [cyan]{package}[/cyan]...")
        
        try:
            cmd = [sys.executable, "-m", "pip", "uninstall", "-y"] + targets
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            console.print(f"[bold green]✓ Success![/bold green] Removed {package} successfully.")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]✗ Error: Remove fail ho gaya![/bold red]")
            console.print(f"[dim]{e.stderr}[/dim]")

    @staticmethod
    def update(package: str) -> None:
        """Update a package."""
        targets = PACKAGE_MAP.get(package, [package])
        
        console.print(f"[bold green]📦 JugaadLang Package Manager[/bold green]")
        console.print(f"Updating [cyan]{package}[/cyan]...")
        
        try:
            cmd = [sys.executable, "-m", "pip", "install", "--upgrade"] + targets
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            console.print(f"[bold green]✓ Success![/bold green] Updated {package} successfully.")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]✗ Error: Update fail ho gaya![/bold red]")
            console.print(f"[dim]{e.stderr}[/dim]")

    @staticmethod
    def search(query: str) -> None:
        """Search PyPI or local JugaadLang package map for query."""
        console.print(f"[bold green]📦 JugaadLang Package Manager Search[/bold green]")
        console.print(f"Searching for '[yellow]{query}[/yellow]'...\n")
        
        # Check built-in stdlib mapping first
        builtin_matches = []
        for name, deps in PACKAGE_MAP.items():
            if query.lower() in name.lower() or any(query.lower() in d.lower() for d in deps):
                builtin_matches.append((name, ", ".join(deps), "JugaadLang Bundle"))
                
        # Also check local standard libraries
        local_stdlibs = ["ganit", "web", "faili", "json", "samay", "tantra", "crypto", "database", "chai", "jokes", "motivation", "fortune", "memes", "catfacts"]
        for lib in local_stdlibs:
            if query.lower() in lib.lower():
                builtin_matches.append((lib, "None (Built-in)", "JugaadLang Stdlib"))

        table = Table(title=f"Search Results for '{query}'")
        table.add_column("Package Name", style="cyan")
        table.add_column("Dependencies / Details", style="magenta")
        table.add_column("Source", style="green")

        for match in builtin_matches:
            table.add_row(*match)

        # Query PyPI API as fallback
        try:
            url = f"https://pypi.org/pypi/{query}/json"
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                data = response.json()
                info = data.get("info", {})
                table.add_row(info.get("name", query), info.get("summary", "No description"), "PyPI")
        except Exception:
            pass # Ignore PyPI failures, standard library matches are primary

        if table.row_count > 0:
            console.print(table)
        else:
            console.print(f"[yellow]Mila nahi! Koi package nahi mila matching '{query}'[/yellow]")
