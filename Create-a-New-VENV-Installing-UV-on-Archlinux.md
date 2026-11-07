LOG: [LEARN] Guide: Create Python Virtual Environment with UV on Arch Linux

**Title:** Create a New VENV Installing UV on Archlinux
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Create-a-New-VENV-Installing-UV-on-Archlinux.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux
- Internet connection

### Step 1: Install UV
```bash
# Official installer (recommended)
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pacman
$ sudo pacman -S uv

# Or via pip
$ pip install uv
```

### Step 2: Verify Installation
```bash
$ uv --version
```

### Step 3: Create Virtual Environment
```bash
$ uv venv .venv
```

### Step 4: Activate Environment
```bash
$ source .venv/bin/activate
# Prompt changes to show (.venv)
```

### Step 5: Install Dependencies
```bash
# From requirements.txt
$ uv pip install -r requirements.txt

# Or add packages directly
$ uv pip install package1 package2
```

### Step 6: Run Project
```bash
$ uv run python main.py
# Or with activated env:
$ python main.py
```

## The "Blueprint" (The Why/Logic)

### UV Commands Map
| UV Command | Equivalent |
|------------|------------|
| `uv venv` | `python -m venv` |
| `uv pip install` | `pip install` |
| `uv pip sync` | `pip install -r requirements.txt` |
| `uv run` | Runs in venv without activation |
| `uv add` | Add to pyproject.toml (projects) |

### Project vs Virtual Environment
- `uv init` — creates project with `pyproject.toml`
- `uv venv` — creates standalone virtual environment

### Python Version Selection
```bash
$ uv python list              # List available
$ uv python install 3.12      # Install version
$ uv venv --python 3.12 .venv # Use specific version
```

## The "Deep Dive" (The Technical Root)

### UV Architecture
- Written in Rust, single binary
- Uses hard links for global cache (`~/.cache/uv`)
- Parallel operations, minimal overhead

### Cache Management
```bash
$ uv cache clean          # Remove cache
$ uv cache dir            # Show cache location
```

### Lockfile
- `uv.lock` — cross-platform lockfile
- `requirements.txt` — compatible export

### References
- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub](https://github.com/astral-sh/uv)
- [PEP 621](https://peps.python.org/pep-0621/) — pyproject.toml standard