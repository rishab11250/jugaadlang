# Changelog

All notable changes to the **JugaadLang** VS Code extension are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-06-09

> *"Pehla kadam — sabse mushkil hota hai, lekin yeh toh ekdum mast tha!"* 🎉

### 🎉 Added — The Grand Debut

#### Syntax Highlighting
- Complete TextMate grammar (`source.jug`) covering all JugaadLang constructs
- **Control flow keywords**: `agar`, `shayad`, `warna`, `ghumo`, `jabtak`, `rukja`, `chalte_raho`, `wapas`, `theek_hai`
- **Declaration keywords**: `banao`, `ustad`, `chota_funkshan`
- **Exception keywords**: `koshish`, `gadbad`, `aakhir_me`, `udao`
- **Async keywords**: `tez`, `intezaar`, `baanto`
- **Logical operators**: `aur`, `ya`, `nahi`, `mein`, `hai`, `mein_nahi`, `nahi_hai`
- **Import keywords**: `lao`, `se`
- **Language constants**: `sahi` (True), `galat` (False), `kuch_nahi` (None)
- **Built-in functions**: `bolo`, `poochho`, `range`, `len`, `str`, `int`, `float`, and many more
- **JugaadLang stdlib**: `chai`, `himmat`, `ghaas_chhoo`, `bachao`, `fortune`, `jugaad`
- **Variable language**: `khud` (self)
- **F-strings** with embedded expression highlighting
- **Triple-quoted strings** (`"""` and `'''`)
- **All comment styles**: `#`, `//`, `/* */`
- **Numeric literals**: integers, floats, hex (`0x`), binary (`0b`), octal (`0o`), complex numbers
- **Decorators** (`@decorator_name`)
- **Magic methods** (`__init__`, `__str__`, etc.)
- **String escape sequences** (`\n`, `\t`, `\uXXXX`, etc.)
- **Punctuation scopes** for `()`, `[]`, `{}`, `:`, `,`, `.`

#### Hover Tooltips
- Hover over any JugaadLang keyword to see:
  - Python equivalent
  - English description of what it does
  - A funny Hindi phrase (because why not!)
- Full coverage for all 30+ JugaadLang keywords and built-ins

#### Code Snippets (25+ snippets)
- `hello` — Hello World (`Namaste Duniya! 🇮🇳`)
- `bolo` — print statement
- `agar`, `agar-warna`, `agar-shayad-warna` — conditional blocks
- `banao`, `tez-banao` — function and async function definitions
- `ustad`, `class-inherit` — class definitions
- `ghumo`, `ghumo-range` — for loops
- `jabtak` — while loop
- `koshish`, `koshish-aakhir`, `koshish-full` — exception handling
- `chota_funkshan` — lambda expression
- `baanto` — generator function
- `lao`, `se-lao` — import statements
- `list-ghumo`, `dict-ghumo` — comprehensions
- `main` — main boilerplate
- `fibonacci` — fibonacci function
- `api` — Flask API boilerplate
- `property-banao` — property getter/setter
- `data-ustad` — dataclass
- `banao-typed` — typed function with type hints
- `pakka` — assert statement
- `hatao` — del statement

#### Commands
- **`JugaadLang: Run File`** (`Cmd+F5` / `Ctrl+F5`) — runs `jug run <file>` in integrated terminal
- **`JugaadLang: Open REPL`** — opens `jug repl` in integrated terminal
- **▶ Play button** in editor title bar for `.jug` files

#### Status Bar
- Shows `🇮🇳 JugaadLang — <filename>` when a `.jug` file is active
- Click to run the current file
- Auto-hides when non-JugaadLang file is focused

#### Language Configuration
- Comment toggling (`#` line comments, `/* */` block comments)
- Auto-closing pairs for `()`, `[]`, `{}`, `""`, `''`, `"""`, `'''`
- Surrounding pairs
- Smart indentation rules (indent after `:`)
- Decrease indent for `warna`, `shayad`, `gadbad`, `aakhir_me`
- Offside rule folding (indentation-based)

#### Extension Settings
- `jugaadlang.jugPath` — configure path to `jug` executable
- `jugaadlang.showWelcomeMessage` — toggle welcome message

#### Welcome Message
- Friendly welcome message on first `.jug` file open
- One-time display (stored in global state)
- Quick actions: "Run File", "Open REPL"

---

## [Unreleased]

### Planned Features
- 🔍 Go-to-definition support
- 🔄 Auto-formatter integration (`jug fmt`)
- 🧪 Test runner integration
- 📊 Code lens for function complexity
- 🌐 IntelliSense / completion provider
- 🐛 Debugger support
- 📦 Package manager integration (`jugpkg`)
- 🎨 Custom color themes optimized for JugaadLang

---

*"Pehla version toh bas shuruat hai — asli jugaad abhi baki hai!"* 🔧
