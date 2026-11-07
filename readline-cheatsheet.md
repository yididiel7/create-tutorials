LOG: [LEARN] Reference: Readline Emacs Editing Mode Cheatsheet

**Title:** Readline Cheatsheet
**Date:** 2023-12-29
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** readline-cheatsheet.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Key Notation
| Symbol | Key |
|--------|-----|
| `C-` | Ctrl |
| `M-` | Alt (Meta) |
| `DEL` | Backspace |

### Essentials
| Binding | Action |
|---------|--------|
| `C-b` | Move back one character |
| `C-f` | Move forward one character |
| `DEL` | Delete character left of cursor |
| `C-d` | Delete character under cursor |
| `C-_` | Undo last change |

### Movement
| Binding | Action |
|---------|--------|
| `C-a` | Move to start of line |
| `C-e` | Move to end of line |
| `M-f` | Move forward one word |
| `M-b` | Move backward one word |
| `C-l` | Clear screen, reprint line at top |

### Killing (Cutting)
| Binding | Action |
|---------|--------|
| `C-k` | Kill to end of line |
| `M-d` | Kill to end of word |
| `M-DEL` | Kill to start of word |
| `C-w` | Kill to previous whitespace |

### Yanking (Pasting)
| Binding | Action |
|---------|--------|
| `C-y` | Yank most recent kill |
| `M-y` | Rotate kill-ring, yank new top |

### History
| Binding | Action |
|---------|--------|
| `C-p` | Previous history line (up) |
| `C-n` | Next history line (down) |
| `M-<` | First history line |
| `M->` | Last history line (current input) |
| `C-r` | Reverse incremental search |
| `C-s` | Forward incremental search |
| `M-p` | Reverse non-incremental search |
| `M-n` | Forward non-incremental search |
| `M-C-y` | Insert first arg of previous command |
| `M-.` / `M-_` | Insert last arg of previous command |

## The "Blueprint" (The Why/Logic)

### Readline in Shells
- **Bash**: Uses readline by default
- **Zsh**: Uses ZLE (Zsh Line Editor), similar but different bindings
- **Python REPL**: Uses readline if available
- **Many CLI tools**: Use readline for input editing

### Emacs vs Vi Mode
```bash
# Emacs mode (default in bash)
set -o emacs

# Vi mode
set -o vi
# ESC to enter command mode
# Standard vi keys: h/j/k/l, w/b/e, etc.
```

### Kill Ring vs Clipboard
- **Kill ring**: Internal readline buffer (C-y, M-y)
- **System clipboard**: Separate, use terminal copy/paste
- Kill ring persists within shell session only

## The "Deep Dive" (The Technical Root)

### Readline Library
- GNU Readline provides line editing for interactive programs
- Used by: bash, python, psql, sqlite3, gdb, etc.
- Config: `~/.inputrc`

### Customizing `~/.inputrc`
```bash
# Example customizations
"\C-p": history-search-backward
"\C-n": history-search-forward
"\e[A": history-search-backward  # Up arrow
"\e[B": history-search-forward   # Down arrow

# Better completion
set show-all-if-ambiguous on
set completion-ignore-case on
```

### Vi Mode Bindings (Command Mode)
| Key | Action |
|-----|--------|
| `h`/`l` | Left/right character |
| `w`/`b` | Forward/back word |
| `0`/`$` | Start/end of line |
| `dw` | Delete word |
| `dd` | Delete line |
| `cc` | Change line |
| `p`/`P` | Paste after/before |
| `u` | Undo |
| `.` | Repeat last change |

### Search in Vi Mode
| Key | Action |
|-----|--------|
| `/` | Search backward |
| `?` | Search forward |
| `n` | Next match |
| `N` | Previous match |

### References
- `man readline`
- `man bash` (READLINE section)
- [GNU Readline Manual](https://tiswww.case.edu/php/chet/readline/rluserman.html)
- [Zsh ZLE Manual](https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html)