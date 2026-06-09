# Changelog

All notable changes to **JugaadLang** will be documented in this file.

## [1.0.0] - 2026-06-09

### Added
- **Core Syntax & Compiler**:
  - Implemented 1:1 direct compilation from JugaadLang AST to native Python AST.
  - Added **Structural Pattern Matching** (`agar_match` / `kaand`) syntax translating to Python 3.10+ pattern matching block structures.
  - Implemented full block parser, async/await constructs, slicing, lambda expressions (`chota_funkshan`), and list/dict/set comprehensions.
  
- **Standard Mapped Built-ins**:
  - Registered 35+ Roman-Hindi wrappers for standard Python built-ins (e.g., `prakar` for `type`, `lambaee` for `len`, `suchi` for `list`, `kosh` for `dict`, `maan` for `abs`, `subclass_hai` for `issubclass`).
  - Added 8 new interactive funny built-in functions:
    - `nazar()`: Blocks compiler bad vibes and bugs.
    - `ashirwad()`:Elder blessings for guaranteed successful runtime runs.
    - `dhanya_waad()`: Polite desi gratitude output.
    - `bhagwan_bhala_kare()`: Divine intervention prayer request for compilers.
    - `paisa_wasool()`: Value verification for free open-source software.
    - `bas_kar_bhai()`: Prompt to shutdown laptop and sleep.
    - `chilla_mat()`: Reminder to calm down and relax while debugging.
    - `kundli()`: Code horoscopic analysis highlighting loop blocking transits.

- **Standard Library Features**:
  - **JugaadORM (`database`)**: SQLite-backed ORM supporting database table migrations, MRO-aware class resolving, and transaction rollbacks.
  - **JugaadWeb (`web`)**: Micro REST framework routing via `@web.agar_route` decorator, Flask query/body parsing, and auto JSON serialization.
  - Core modules: `ganit` (maths), `faili` (files), `json`, `samay` (datetime), `tantra` (system), and `crypto`.

- **CLI & Packaging**:
  - Added static typechecker command `jug typecheck` running `mypy` behind the scenes.
  - Implemented package manager locking generating `jug.lock`.
  - Added script arguments pass-through to environment under `sys.argv`/`tantra.argv`.
  - Added root `run.sh` script to streamline testing, packing, and local editable installs.

- **VS Code Extension**:
  - Compiled and packaged extension files into a standalone `.vsix` installer.
  - Included TextMate grammar for highlighting, TS extension for hover docstrings, and a custom circular JL App Logo.

- **Landing Website**:
  - Implemented interactive code tabs highlighting loops, OOP, pattern matching, and JugaadWeb servers.
  - Added copyable terminals with clipboards.
  - Fixed stats grid layouts and preserved space-indentation styling.

### Fixed
- **CI/CD Pipeline**: Corrected setup-python GitHub Action path to `actions/setup-python@v5` and added Python 3.14 coverage.
- **Indentation collapse**: Patched website CSS by applying `white-space: pre` to avoid browser space-collapsing, restoring Python-like indentation formatting.
