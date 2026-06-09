"""
web — JugaadLang Web client requests and micro web framework (JugaadWeb).
"""
from __future__ import annotations
import sys
import os
import requests
from typing import Any, Callable

# Re-export client requests
get = requests.get
post = requests.post
put = requests.put
delete = requests.delete


class JugaadWeb:
    """
    JugaadWeb — The official micro web framework for JugaadLang.
    Wraps Flask if available, falls back to Python's standard http.server otherwise.
    """

    def __init__(self) -> None:
        self.routes: dict[str, tuple[Callable, list[str]]] = {}
        try:
            from flask import Flask
            self.flask_app = Flask("JugaadWeb")
        except ImportError:
            self.flask_app = None

    def route(self, path: str, methods: list[str] = ["GET"]) -> Callable:
        """Register a route decorator."""
        def decorator(func: Callable) -> Callable:
            self.routes[path] = (func, methods)
            if self.flask_app:
                # Register route in Flask
                self.flask_app.add_url_rule(path, func.__name__, func, methods=methods)
            return func
        return decorator

    def run(self, port: int = 5000, host: str = "127.0.0.1") -> None:
        """Start the web server."""
        if self.flask_app:
            print(f"🚀 JugaadWeb is running on http://{host}:{port} using Flask backend!")
            self.flask_app.run(host=host, port=port, debug=False)
        else:
            print("⚠️ Flask is not installed. Falling back to basic Python http.server.")
            print("💡 Tip: Install Flask for full web features: `jug install web` or `pip install flask`.\n")
            print(f"🚀 JugaadWeb running on http://{host}:{port}...")
            
            from http.server import BaseHTTPRequestHandler, HTTPServer
            
            # Save self reference for handler
            routes_map = self.routes
            
            class JugaadHTTPHandler(BaseHTTPRequestHandler):
                def log_message(self, format_str: str, *args: Any) -> None:
                    # Suppress default server logs for cleaner output
                    pass
                
                def do_GET(self) -> None:
                    # Find matching route
                    func_tuple = routes_map.get(self.path)
                    if func_tuple and "GET" in func_tuple[1]:
                        try:
                            res = func_tuple[0]()
                            self.send_response(200)
                            self.send_header("Content-type", "text/html; charset=utf-8")
                            self.end_headers()
                            self.wfile.write(str(res).encode("utf-8"))
                        except Exception as e:
                            self.send_response(500)
                            self.end_headers()
                            self.wfile.write(f"Server error: {e}".encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(b"404 - Route gayab ho gaya!")
            
            server = HTTPServer((host, port), JugaadHTTPHandler)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("\n🛑 Server stopped.")
                server.server_close()


# Global default app instance
_default_app = JugaadWeb()


def agar_route(path: str, methods: list[str] = ["GET"]) -> Callable:
    """Decorator to register a route on the default global app."""
    return _default_app.route(path, methods)


def chalao(port: int = 5000, host: str = "127.0.0.1") -> None:
    """Start the default global app web server."""
    _default_app.run(port=port, host=host)
