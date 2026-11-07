LOG: [LEARN] Guide: Tmuxifier Quick Start and Zsh Integration Fix

**Title:** Tmuxifier Quick Start Fix
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Tmuxifier-Quick-Start-fix.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Tmux installed
- Git installed
- Shell (zsh/bash) with `$EDITOR` set

### Install Tmuxifier
```bash
# Clone repository
$ git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier

# Add to PATH (before tmuxifier init!)
# ~/.zshrc or ~/.bashrc
export PATH="$HOME/.tmuxifier/bin:$PATH"

# Initialize tmuxifier
eval "$(tmuxifier init -)"

# Restart shell
$ source ~/.zshrc
```

### Verify Installation
```bash
$ tmuxifier help
$ tmuxifier list
```

### Zsh Integration Fix
```bash
# CRITICAL: PATH must be set BEFORE eval "$(tmuxifier init -)"
# In ~/.zshrc, ensure this order:

# 1. PATH configuration (early)
export PATH="$HOME/.tmuxifier/bin:$PATH"
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
# ... other PATH exports

# 2. Tool initialization (after PATH)
eval "$(tmuxifier init -)"
eval "$(zoxide init --cmd cd zsh)"
eval "$(fzf --zsh)"
# ... other eval statements

# 3. Aliases and functions (last)
```

### Common Issue: "command not found: tmuxifier"
**Cause**: `eval "$(tmuxifier init -)"` runs before `$HOME/.tmuxifier/bin` is in PATH
**Fix**: Move PATH export above the eval line

## The "Recipe" (Tmuxifier Usage)

### Core Commands
```bash
# Help and listing
$ tmuxifier help
$ tmuxifier list
$ tmuxifier list-windows
$ tmuxifier list-sessions

# Window layouts
$ tmuxifier new-window my-dev-window    # Create (opens in $EDITOR)
$ tmuxifier load-window my-dev-window   # Load in current session
$ tmuxifier edit-window my-dev-window   # Edit existing

# Session layouts
$ tmuxifier new-session my-project
$ tmuxifier load-session my-project
$ tmuxifier edit-session my-project
```

### Window Layout Example
```bash
# ~/.tmuxifier/layouts/my-dev-window.window.sh
window_root "~/projects/myapp"
new_window "My Dev Window"
split_v 20                       # 20% bottom pane
run_cmd "npm run dev"            # Command in bottom
split_h 50                       # 50% right pane
run_cmd "nvim"                   # Editor in right
select_pane 0                    # Focus first pane
```

### Session Layout Example
```bash
# ~/.tmuxifier/layouts/my-project.session.sh
session_root "~/projects/myapp"
new_session "my-project"

# Load existing window layouts
load_window "editor"
load_window "logs"

# Or define inline
new_window "server"
run_cmd "npm start"
```

### Layout Commands Reference
| Command | Description |
|---------|-------------|
| `window_root "path"` | Set window working directory |
| `new_window "name"` | Create window with title |
| `split_v [percent]` | Vertical split (bottom %) |
| `split_h [percent]` | Horizontal split (right %) |
| `run_cmd "cmd"` | Run command in current pane |
| `select_pane [index]` | Focus pane (0-based) |
| `session_root "path"` | Set session working directory |
| `new_session "name"` | Create session |
| `load_window "name"` | Load existing window layout |

### Layout Storage
```
~/.tmuxifier/layouts/
├── *.window.sh    # Window layouts
└── *.session.sh   # Session layouts
```

### Test Configuration
```bash
$ source ~/.zshrc
$ tmuxifier help  # Should work without errors
```

## The "Blueprint" (The Why/Logic)

### Initialization Order Matters
```
PATH exports → eval init → aliases/functions
     ↑              ↑              ↑
  Binaries     Completion     User custom
  available    functions      definitions
```

### Why PATH Before Init?
- `tmuxifier init -` generates shell functions/completions
- Functions may reference `tmuxifier` binary
- Without PATH, completions fail to register

### Zinit Users: Proper Plugin Order
```zsh
# In .zshrc with Zinit
zinit ice wait'!' lucid
zinit light jimeh/tmuxifier

# OR manual (more control):
export PATH="$HOME/.tmuxifier/bin:$PATH"
eval "$(tmuxifier init -)"
```

## The "Deep Dive" (The Technical Root)

### tmuxifier init Output
```bash
$ tmuxifier init -
# Generates shell code:
# - tmuxifier() function wrapper
# - Completion functions (_tmuxifier)
# - Aliases (tf=tmuxifier)
```

### Layout Script Execution
```bash
# When you run: tmuxifier load-window foo
# 1. Sources ~/.tmuxifier/layouts/foo.window.sh
# 2. Executes commands in current tmux session
# 3. Commands: new_window, split_v, run_cmd, etc.
```

### Layout Commands Internals
| Command | Implementation |
|---------|----------------|
| `new_window` | `tmux new-window -n "name"` |
| `split_v N` | `tmux split-window -v -p N` |
| `split_h N` | `tmux split-window -h -p N` |
| `run_cmd` | `tmux send-keys "cmd" Enter` |
| `select_pane N` | `tmux select-pane -t N` |

### File Locations
```
~/.tmuxifier/
├── bin/tmuxifier          # Main script
├── layouts/
│   ├── *.window.sh        # Window layouts
│   └── *.session.sh       # Session layouts
└── completions/           # Shell completions
```

### References
- [Tmuxifier GitHub](https://github.com/jimeh/tmuxifier)
- `tmuxifier help`
- [Tmux Manual](https://github.com/tmux/tmux/wiki)