# 🇮🇳 JugaadLang VS Code Extension

> **Desi coding ka asli maza — ab VS Code mein!**

The official Visual Studio Code extension for **JugaadLang** — a Python-powered programming language that uses Roman Hindi keywords. Write code in your mother tongue's spirit and let the compiler do the jugaad!

---

## ✨ Features

### 🎨 Syntax Highlighting
Full TextMate grammar coverage for every JugaadLang construct:

| Category | Keywords |
|---|---|
| **Control Flow** | `agar`, `shayad`, `warna`, `rukja`, `chalte_raho`, `wapas` |
| **Loops** | `ghumo`, `jabtak` |
| **Functions & Classes** | `banao`, `ustad`, `chota_funkshan` |
| **Exceptions** | `koshish`, `gadbad`, `aakhir_me`, `udao` |
| **Async** | `tez`, `intezaar`, `baanto` |
| **Operators** | `aur`, `ya`, `nahi`, `mein`, `hai` |
| **Imports** | `lao`, `se` |
| **Constants** | `sahi`, `galat`, `kuch_nahi` |
| **Built-ins** | `bolo`, `poochho`, `range`, `len`, `str`, ... |

- ✅ F-strings with embedded expression highlighting
- ✅ Triple-quoted strings (`"""` and `'''`)
- ✅ Comments (`#`, `//`, `/* */`)
- ✅ Hex, binary, octal, float numerics
- ✅ Decorators (`@`)
- ✅ Magic methods (`__init__`, etc.)
- ✅ String escape sequences

---

### 💡 Hover Tooltips
Hover over **any JugaadLang keyword** to see:
- 🔤 The Python equivalent
- 📖 A description of what it does
- 😄 A funny Hindi phrase to brighten your day

**Example hover for `koshish`:**
```
🇮🇳 koshish — JugaadLang Keyword

Python equivalent: try

Try block — attempt to execute potentially failing code.

---
💪 "Koshish karne walon ki kabhi haar nahi hoti!"
```

---

### 📝 Code Snippets
Type these prefixes and press `Tab` for instant boilerplate:

| Prefix | Expands To |
|---|---|
| `hello` | Hello World (`Namaste Duniya! 🇮🇳`) |
| `bolo` | `bolo("...")` |
| `agar` | if block |
| `agar-warna` | if/else block |
| `agar-shayad-warna` | if/elif/else block |
| `banao` | function definition |
| `tez-banao` | async function |
| `ustad` | class with `shuru` |
| `class-inherit` | class with inheritance |
| `ghumo` | for loop |
| `ghumo-range` | for with range |
| `jabtak` | while loop |
| `koshish` | try/except |
| `koshish-aakhir` | try/except/finally |
| `koshish-full` | try/except/else/finally |
| `chota_funkshan` | lambda expression |
| `baanto` | generator function |
| `lao` | import |
| `se-lao` | from ... import |
| `list-ghumo` | list comprehension |
| `dict-ghumo` | dict comprehension |
| `main` | main boilerplate |
| `fibonacci` | fibonacci function |
| `api` | Flask API boilerplate |
| `property-banao` | property getter/setter |
| `data-ustad` | dataclass |
| `banao-typed` | typed function |

---

### ▶️ Run File Command
**Keyboard Shortcut:** `Cmd+F5` (Mac) / `Ctrl+F5` (Windows/Linux)

Or use the **▶ play button** in the editor title bar when a `.jug` file is active.

Runs `jug run <current-file>` in an integrated terminal.

---

### 🖥️ Open REPL
**Command Palette:** `JugaadLang: Open REPL`

Opens an interactive JugaadLang REPL session with `jug repl`.

---

### 📊 Status Bar
When a `.jug` file is open, the status bar shows:

```
🇮🇳 JugaadLang — filename.jug
```

Click it to run the current file!

---

### 🎉 Welcome Message
On first use, a friendly welcome message appears:
> *"JugaadLang mein aapka swagat hai! Desi coding ka asli maza shuru hota hai abhi!"*

---

## 🚀 Getting Started

### 1. Install JugaadLang
```bash
pip install jugaadlang
# or
git clone https://github.com/jugaadlang/jugaadlang
cd jugaadlang && pip install -e .
```

### 2. Create Your First File
Create `namaste.jug`:
```
bolo("Namaste Duniya! 🇮🇳")

banao fibonacci(n):
    agar n <= 1:
        wapas n
    wapas fibonacci(n - 1) + fibonacci(n - 2)

ghumo i mein range(10):
    bolo(f"fib({i}) = {fibonacci(i)}")
```

### 3. Run It
Press `Cmd+F5` or click the **▶** button!

---

## ⚙️ Extension Settings

| Setting | Default | Description |
|---|---|---|
| `jugaadlang.jugPath` | `"jug"` | Path to the `jug` executable |
| `jugaadlang.showWelcomeMessage` | `true` | Show welcome message on first `.jug` file |

---

## 🔑 Complete Keyword Reference

| JugaadLang | Python | Meaning |
|---|---|---|
| `bolo` | `print` | Say / Speak |
| `poochho` | `input` | Ask |
| `agar` | `if` | If |
| `shayad` | `elif` | Maybe |
| `warna` | `else` | Otherwise |
| `ghumo` | `for` | Roam / Loop |
| `jabtak` | `while` | Until |
| `banao` | `def` | Make / Create |
| `wapas` | `return` | Return / Come back |
| `ustad` | `class` | Teacher / Master |
| `khud` | `self` | Self |
| `lao` | `import` | Bring |
| `se` | `from` | From |
| `rukja` | `break` | Stop right there |
| `chalte_raho` | `continue` | Keep going |
| `koshish` | `try` | Try / Attempt |
| `gadbad` | `except` | Problem / Chaos |
| `aakhir_me` | `finally` | In the end |
| `udao` | `raise` | Fly / Launch |
| `sahi` | `True` | Correct |
| `galat` | `False` | Wrong |
| `kuch_nahi` | `None` | Nothing |
| `aur` | `and` | And |
| `ya` | `or` | Or |
| `nahi` | `not` | No / Not |
| `tez` | `async` | Fast |
| `intezaar` | `await` | Wait |
| `baanto` | `yield` | Share / Distribute |
| `theek_hai` | `pass` | It's okay / Fine |
| `sabka` | `global` | Everyone's / Global |
| `chota_funkshan` | `lambda` | Small function |
| `mein` | `in` | In |
| `bulawo` | *(call)* | Call / Summon |

---

## 📜 License

MIT © JugaadLang Contributors

---

*"Code likhna mushkil nahi — bas sahi jugaad chahiye!"* 🔧
