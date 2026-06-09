"""
Tests for JugaadLang Runtime/Interpreter.
"""
import pytest
import os
from jugaadlang.runtime.interpreter import JugaadInterpreter


def test_interpreter_exec():
    interpreter = JugaadInterpreter()
    interpreter.run("x = 5\ny = x + 10")
    assert interpreter.globals["x"] == 5
    assert interpreter.globals["y"] == 15


def test_interpreter_eval_expr():
    interpreter = JugaadInterpreter()
    res = interpreter.run_expression("10 * 2 + 5")
    assert res == 25


def test_interpreter_builtins(capsys):
    interpreter = JugaadInterpreter()
    interpreter.run("chai()")
    captured = capsys.readouterr()
    assert "Chai piyo!" in captured.out or "Chai pi lo" in captured.out


def test_interpreter_stdlib():
    interpreter = JugaadInterpreter()
    interpreter.run("lao ganit\nx = ganit.sqrt(16)")
    assert interpreter.globals["x"] == 4.0


def test_class_inheritance():
    interpreter = JugaadInterpreter()
    code = """
ustad Parent:
    banao shuru(khud, val):
        khud.val = val
    banao show(khud):
        wapas khud.val

ustad Child(Parent):
    banao show_double(khud):
        wapas khud.show() * 2

c = Child(10)
res_val = c.show_double()
"""
    interpreter.run(code)
    assert interpreter.globals["res_val"] == 20


def test_comprehensions_and_loops():
    interpreter = JugaadInterpreter()
    code = """
# List comprehension
vals = [x * 2 ghumo x mein range(5)]
# Dict comprehension
d_vals = {x: x * 3 ghumo x mein range(3)}
# Set comprehension
s_vals = {x ghumo x mein range(3)}
# Ternary expression
res = "yes" agar sahi warna "no"
"""
    interpreter.run(code)
    assert interpreter.globals["vals"] == [0, 2, 4, 6, 8]
    assert interpreter.globals["d_vals"] == {0: 0, 1: 3, 2: 6}
    assert interpreter.globals["s_vals"] == {0, 1, 2}
    assert interpreter.globals["res"] == "yes"


def test_try_except_runtime():
    interpreter = JugaadInterpreter()
    code = """
caught = galat
koshish:
    x = 10 / 0
gadbad ZeroDivisionError:
    caught = sahi
"""
    interpreter.run(code)
    assert interpreter.globals["caught"] is True


def test_jugaad_orm():
    # Clean up DBs before start
    for db in ("jugaad.db", "test_jugaad.db"):
        if os.path.exists(db):
            os.remove(db)

    interpreter = JugaadInterpreter()
    code = """
lao database
database.Model._db_path = "test_jugaad.db"

ustad Person(database.Model):
    name = database.String()
    age = database.Integer()

Person.banao_table()
p1 = Person(name="Aman", age=25)
p1.bachao()

results = Person.filter(name="Aman")
res_len = len(results)
res_name = results[0].name
res_age = results[0].age
"""
    try:
        interpreter.run(code)
        assert interpreter.globals["res_len"] == 1
        assert interpreter.globals["res_name"] == "Aman"
        assert interpreter.globals["res_age"] == 25
    finally:
        # Clean up test DB
        for db in ("jugaad.db", "test_jugaad.db"):
            if os.path.exists(db):
                os.remove(db)


def test_jugaad_web():
    interpreter = JugaadInterpreter()
    code = """
lao web
@web.agar_route("/test")
banao hello_test():
    wapas "working"
"""
    interpreter.run(code)
    
    # Verify that the route was correctly registered in web default app
    import sys
    web_module = sys.modules["web"]
    assert "/test" in web_module._default_app.routes
    handler, methods = web_module._default_app.routes["/test"]
    assert handler() == "working"
    assert "GET" in methods
