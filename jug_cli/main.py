"""
JugaadLang CLI Main Entry Point.
"""
from __future__ import annotations
import click
import os
import sys
import ast
from rich.console import Console

from jugaadlang.repl.repl import JugaadREPL
from jugaadlang.runtime.interpreter import JugaadInterpreter
from jugaadlang.package_manager.manager import JugaadPackageManager

console = Console(color_system="truecolor", force_terminal=True)


@click.group()
@click.version_option(version="1.0.0", message="JugaadLang v%(version)s 🇮🇳")
def main() -> None:
    """JugaadLang — The Hindi-keyword programming language. 🚀"""
    pass


@main.command()
@click.argument("file", type=click.Path(exists=True))
def run(file: str) -> None:
    """Run a JugaadLang (.jug) file."""
    if not file.endswith(".jug"):
        console.print("[yellow]⚠️ Warning: File extension is not '.jug'. Running it anyway.[/yellow]")
        
    try:
        with open(file, "r", encoding="utf-8") as f:
            source = f.read()
            
        interpreter = JugaadInterpreter(filename=file)
        interpreter.run(source)
    except Exception:
        sys.exit(1)


@main.command()
def repl() -> None:
    """Start the JugaadLang interactive REPL."""
    try:
        r = JugaadREPL()
        r.start()
    except KeyboardInterrupt:
        console.print("\n[bold orange1]Namaste! Chalte hain! 🙏[/bold orange1]")


@main.command()
@click.argument("package")
def install(package: str) -> None:
    """Install a package or custom bundle (e.g. 'web')."""
    JugaadPackageManager.install(package)


@main.command()
@click.argument("package")
def remove(package: str) -> None:
    """Uninstall a package."""
    JugaadPackageManager.remove(package)


@main.command()
@click.argument("package")
def update(package: str) -> None:
    """Update a package."""
    JugaadPackageManager.update(package)


@main.command()
@click.argument("query")
def search(query: str) -> None:
    """Search for packages."""
    JugaadPackageManager.search(query)


@main.command()
@click.argument("project_name")
def new(project_name: str) -> None:
    """Create a new JugaadLang project boilerplate."""
    console.print(f"[bold green]✨ Naya Project Banao:[/bold green] Creating folder '{project_name}'...")
    
    if os.path.exists(project_name):
        console.print(f"[bold red]✗ Error: Directory '{project_name}' pehle se hi hai![/bold red]")
        sys.exit(1)
        
    try:
        os.makedirs(project_name)
        
        # Write main.jug boilerplate
        main_jug_content = (
            '# JugaadLang Project Boilerplate\n\n'
            'bolo("Namaste Duniya! 🙏")\n\n'
            'poochho naam\n'
            'agar naam == "Sumangal":\n'
            '    bolo("Legend mil gaya 😎")\n'
            'warna:\n'
            '    bolo("Hello " + naam)\n'
        )
        with open(os.path.join(project_name, "main.jug"), "w", encoding="utf-8") as f:
            f.write(main_jug_content)
            
        # Write README
        readme_content = (
            f"# {project_name}\n\n"
            f"JugaadLang project created successfully.\n\n"
            f"Run the project using:\n"
            f"```bash\n"
            f"jug run main.jug\n"
            f"```\n"
        )
        with open(os.path.join(project_name, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        console.print(f"[bold green]✓ Success![/bold green] Project '{project_name}' is ready. Go ahead and hack! 🛠️")
    except Exception as e:
        console.print(f"[bold red]✗ Fail ho gaya: {e}[/bold red]")
        sys.exit(1)


@main.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output file to write transpiled Python code.")
def compile(file: str, output: str | None) -> None:
    """Transpile a JugaadLang (.jug) file to standard Python code."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            source = f.read()
            
        from jugaadlang.lexer.lexer import Lexer
        from jugaadlang.parser.parser import Parser
        from jugaadlang.transformer.to_python import JugaadToPythonTransformer
        
        # Transpile pipeline
        lexer = Lexer(source, file)
        tokens = lexer.tokenize()
        parser = Parser(tokens, file, source)
        ast_mod = parser.parse()
        transformer = JugaadToPythonTransformer(file)
        py_ast = transformer.transform(ast_mod)
        
        # Translate AST to Python source string
        py_source = ast.unparse(py_ast)
        
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(py_source)
            console.print(f"[bold green]✓ Success![/bold green] Compiled to Python: [cyan]{output}[/cyan]")
        else:
            # Print to stdout
            print(py_source)
    except Exception as e:
        console.print(f"[bold red]✗ Transpilation failed[/bold red]", file=sys.stderr)
        sys.exit(1)


@main.command()
@click.argument("file", type=click.Path(exists=True))
def check(file: str) -> None:
    """Validate JugaadLang file syntax without executing it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            source = f.read()
            
        from jugaadlang.lexer.lexer import Lexer
        from jugaadlang.parser.parser import Parser
        
        lexer = Lexer(source, file)
        tokens = lexer.tokenize()
        parser = Parser(tokens, file, source)
        parser.parse()
        
        console.print("[bold green]✓ Code bilkul sahi hai! (Syntax is valid)[/bold green]")
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
