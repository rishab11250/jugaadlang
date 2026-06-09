# JugaadLang Language Specification

JugaadLang is a modern programming language with Roman Hindi keywords, transpiled to Python. It mirrors Python's semantic model and block layout while introducing Hindi equivalents for all core keywords, built-in helper functions, funny diagnostics, and micro-frameworks.

---

## 1. Syntax & Layout

JugaadLang is an indentation-based language. Code blocks are defined by a colon (`:`) followed by a newline and indent.

### 1.1 Indentation
Indentation levels are computed in spaces or tabs (expanded to 8 spaces). Inconsistent indentation (e.g. Mixing spaces and tabs or incorrect dedents) triggers a compiler error.

### 1.2 Comments
JugaadLang supports three comment formats:
* `# comment` — single-line comment (Python style)
* `// comment` — single-line comment (C/JS style)
* `/* comment */` — multi-line/block comment (C/JS style)

---

## 2. Keywords

The compiler tokenizes the following keywords:

| Keyword | Python Equivalent | Purpose |
| :--- | :--- | :--- |
| `bolo` | `print` | Output statement |
| `poochho` | `input` | Input statement / expression |
| `agar` | `if` | Conditional branch |
| `shayad` | `elif` | Secondary conditional branch |
| `warna` | `else` | Fallback conditional branch |
| `ghumo` | `for` | Definite loop |
| `jabtak` | `while` | Indefinite loop |
| `banao` | `def` | Function definition |
| `wapas` | `return` | Function return |
| `ustad` | `class` | Class definition |
| `khud` | `self` | Instance self-reference |
| `lao` | `import` | Module import |
| `se` | `from` | Sub-module import |
| `rukja` | `break` | Loop termination |
| `chalte_raho`| `continue` | Loop skip iteration |
| `koshish` | `try` | Exception try block |
| `gadbad` | `except` | Exception catch block |
| `aakhir_me` | `finally` | Exception cleanup block |
| `udao` | `raise` | Exception raise |
| `sahi` | `True` | Boolean true constant |
| `galat` | `False` | Boolean false constant |
| `kuch_nahi` | `None` | Null constant |
| `aur` | `and` | Logical AND operator |
| `ya` | `or` | Logical OR operator |
| `nahi` | `not` | Logical NOT operator |
| `tez` | `async` | Asynchronous modifier |
| `intezaar` | `await` | Asynchronous wait |
| `baanto` | `yield` | Generator yield |
| `theek_hai` | `pass` | Null statement |
| `sabka` | `global` | Global scope variable |
| `chota_funkshan` | `lambda` | Anonymous inline function |
| `mein` | `in` | Membership operator |
| `hai` | `is` | Identity operator |

---

## 3. Data Types

JugaadLang maps natively to Python's dynamic type system:
* `int`: Arbitrary-precision integer (e.g. `10`, `0xFA`, `0b101`)
* `float`: Double-precision floating-point (e.g. `10.5`, `1e-3`)
* `str`: Unicode string literals (e.g. `"Namaste"`, `'Duniya'`, `f"Hi {naam}"`)
* `bool`: Boolean values (`sahi`, `galat`)
* `null`: Null value (`kuch_nahi`)
* `list`: Resizable array (e.g. `[1, 2, 3]`)
* `tuple`: Immutable array (e.g. `(1, 2, 3)`)
* `dict`: Hash table / map (e.g. `{"naam": "Sumu", "umar": 20}`)
* `set`: Unique set of elements (e.g. `{1, 2, 3}`)

---

## 4. Functions & Classes

### 4.1 Functions (`banao`)
Functions are declared with `banao`. They support default arguments, type annotations, and positional/keyword arguments.
```jugaadlang
banao jod(a: int, b: int = 10) -> int:
    wapas a + b
```

### 4.2 Classes (`ustad`)
Classes are defined with `ustad`. The initialization method must be named `shuru` (which maps to `__init__`). All instance method arguments must specify `khud` (which maps to `self`) as the first argument.
```jugaadlang
ustad Aadmi:
    banao shuru(khud, naam):
        khud.naam = naam
```

---

## 5. built-in Functions

The interpreter automatically injects these interactive functions into the global namespace:
* `chai()`: prints ASCII cup of tea.
* `himmat()`: Prints motivational booster.
* `ghaas_chhoo()`: Prints touch grass advice.
* `bachao()`: Prints emergency help search.
* `fortune()`: Tells a programmer's fortune.
* `jugaad()`: Prints funny debugging tips.
