# JugaadLang 🇮🇳
> Code karo Hindi mein, Duniya hila do! 🚀

JugaadLang is a modern, beginner-friendly, fun programming language inspired by Python, designed for Indian developers. It replaces Python's core keywords with English-spelled Hindi (Roman Hindi) terms and features custom funny error diagnostic outputs, a built-in package manager, and standard libraries.

JugaadLang transpiles directly to native Python AST, meaning it runs with zero runtime performance overhead and provides full compatibility with the entire Python ecosystem.

---

## Table of Contents
1. [Core Philosophy](#core-philosophy)
2. [Installation](#installation)
3. [Language Keywords Reference](#language-keywords-reference)
4. [Example Usage](#example-usage)
5. [Built-in Fun Functions](#built-in-fun-functions)
6. [Ecosystem & Tooling](#ecosystem--tooling)
   - [CLI Runner](#cli-runner)
   - [Interactive REPL](#interactive-repl)
   - [Package Manager](#package-manager)
   - [VS Code Extension](#vs-code-extension)
7. [Standard Library (Stdlib)](#standard-library-stdlib)
8. [Funny Error System](#funny-error-system)
9. [Automated Testing](#automated-testing)

---

## Core Philosophy
1. **Python simplicity:** Clear, indentation-based block syntax.
2. **Hindi-English keywords:** Express logic in the language you think in.
3. **Humorous diagnostics:** Error messages that make you laugh, not crash.
4. **Zero-overhead transpilation:** Compiles to Python bytecode and executes in the native Python VM.

---

## Installation

To install JugaadLang locally:
```bash
# Clone the repository
git clone https://github.com/jugaadlang/jugaadlang.git
cd jugaadlang

# Install in editable mode (or standard install)
pip install -e .
```

Verify that the CLI works:
```bash
jug --version
```

---

## Language Keywords Reference

| Python Keyword | JugaadLang | Hindi Literal Meaning |
| :--- | :--- | :--- |
| `print` | `bolo` | Say / Speak |
| `input` | `poochho` | Ask |
| `if` | `agar` | If |
| `elif` | `shayad` | Maybe / Perhaps |
| `else` | `warna` | Otherwise |
| `for` | `ghumo` | Iterate / Roam |
| `while` | `jabtak` | Until / As long as |
| `def` | `banao` | Create / Make |
| `return` | `wapas` | Return / Back |
| `class` | `ustad` | Master / Teacher |
| `self` | `khud` | Self |
| `import` | `lao` | Import / Bring |
| `from` | `se` | From |
| `break` | `rukja` | Stop! |
| `continue` | `chalte_raho` | Keep going |
| `try` | `koshish` | Try / Attempt |
| `except` | `gadbad` | Problem / Exception |
| `finally` | `aakhir_me` | In the end |
| `raise` | `udao` | Throw / Raise |
| `True` | `sahi` | Correct / True |
| `False` | `galat` | Wrong / False |
| `None` | `kuch_nahi` | Nothing / None |
| `and` | `aur` | And |
| `or` | `ya` | Or |
| `not` | `nahi` | Not |
| `async` | `tez` | Fast / Async |
| `await` | `intezaar` | Wait / Await |
| `yield` | `baanto` | Distribute / Yield |
| `pass` | `theek_hai` | Fine / Pass |
| `global` | `sabka` | Everyone's / Global |
| `lambda` | `chota_funkshan` | Little function |
| `in` | `mein` | In |
| `is` | `hai` | Is |

---

## Example Usage

### 1. Simple Control Flow (`hello.jug`)
```jugaadlang
# Ask for user name
poochho naam

agar naam == "Sumangal":
    bolo("Legend mil gaya! 😎")
warna:
    bolo("Namaste " + naam)
```

Run it:
```bash
jug run hello.jug
```

### 2. Classes & Functions (`oop.jug`)
```jugaadlang
ustad Developer:
    banao shuru(khud, naam, language):
        khud.naam = naam
        khud.language = language

    banao batao(khud):
        bolo(khud.naam + " code likh raha hai " + khud.language + " mein!")

dev = Developer("Sumangal", "JugaadLang")
dev.batao()
```

---

## Built-in Fun Functions
Enjoy several custom interactive built-ins directly at runtime:
* `chai()`: Prints a warm cup of ASCII tea (`☕ Chai pi lo.`)
* `himmat()`: Prints a motivational programming boost (`🔥 Hidden feature detected.`)
* `ghaas_chhoo()`: Gently reminds you to go touch some grass (`🌱 Bahar ghoom aao.`)
* `bachao()`: Starts a mock search for help (`🚨 StackOverflow search shuru.`)
* `fortune()`: Tells a programmer's fortune (`🔮 Bug line 347 mein ho sakta hai.`)
* `jugaad()`: Gives a random hacking/debugging tip.

---

## Ecosystem & Tooling

### CLI Runner
* **Run a file:** `jug run main.jug`
* **Check syntax:** `jug check main.jug`
* **Transpile to Python source:** `jug compile main.jug -o main.py`
* **Create a boilerplate project:** `jug new my_project`

### Interactive REPL
Launch a beautiful interactive terminal shell:
```bash
jug repl
```
Features auto-completion for all keywords, live syntax highlighting, input history, and double-Enter multiline block detection.

### Package Manager
Integrate pip packages or custom bundles:
* **Install:** `jug install web` (installs Flask, requests, httpx, and aiohttp)
* **Remove:** `jug remove web`
* **Update:** `jug update web`
* **Search:** `jug search query`

### VS Code Extension
Launch the extension from `vscode_extension/`. Features full syntax highlighting for `.jug` files, 25+ snippets, hovered keyword documentation in Hindi, and a status bar icon.

---

## Standard Library (Stdlib)

Import standard libraries using `lao` (e.g. `lao ganit`):
1. **`ganit`**: Hindi wrappers for arithmetic/geometry (e.g. `ganit.sin`, `ganit.pi`, `ganit.sqrt`).
2. **`web`**: HTTP request wrappers (`web.get`, `web.post`) and **JugaadWeb** framework with `@web.agar_route("/")` and `web.chalao()`.
3. **`faili`**: Clean file system API (`faili.padho`, `faili.likho`, `faili.jodo`).
4. **`json`**: Native parser (`json.banao_string`, `json.banao_object`).
5. **`samay`**: DateTime operations (`samay.abhibhi()`, `samay.aaj()`, `samay.soja()`).
6. **`tantra`**: Access system variables (`tantra.argv`, `tantra.exit()`, `tantra.platform`).
7. **`crypto`**: Hash encryption (`crypto.sha256`, `crypto.base64_encode`).
8. **`database`**: SQLite ORM (**JugaadORM**) backing tables with `bachao()` and `filter()`.
9. **Fun Libraries**: `chai`, `jokes`, `motivation`, `fortune`, `memes`, `catfacts`.

---

## Funny Error System

Tired of dry Tracebacks? JugaadLang features humorous Hindi exceptions:

#### SyntaxError
```text
🤦 Bhai kya likh diya?
Faili: hello.jug Line 3, Col 12

  agar x ==
            ^

Error Details: Expected value.
Keyboard strike par hai kya?
```

#### NameError
```text
🕵️ Variable 'x' dhundte dhundte thak gaya.
Faili: hello.jug Line 12

  > bolo(x)

Kya gadbad hai?
  'x' mila hi nahi.

Possible reasons:
  • Typo kiya hai
  • Variable declare karna bhool gaye
  • Universe collapse ho gaya
```

#### DivisionByZero
```text
💀 Zero se divide?
Faili: hello.jug Line 5

Kya gadbad hai?
  Newton bhi confuse ho gaya. Maths seekh lo thoda.
```

---

## Automated Testing

To run the full unit test suite:
```bash
# Install development dependencies
pip install -e .[dev]

# Run tests
pytest
```
All tests are configured in the `tests/` directory.
