LOG: [LEARN] Guide: Fix Fabric Zsh Completion Errors

**Title:** Fabric Error Analysis and Shell Completion Review
**Date:** 2026-02-14 (10:12:11 IST)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Fabric-Fixed-Error-Analysis-And-Shell-Completion-Review.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Zsh with completion system (`compinit`)
- Fabric CLI installed (`which fabric`)
- Zsh completion system enabled (`autoload -U compinit && compinit`)

### Root Cause
Two conflicting `_fabric` completion files:
1. `~/.zsh-completions/_fabric` (broken) — loaded first via fpath
2. `/usr/local/share/zsh/site-functions/_fabric` (working) — system installation

### Fix: Remove Broken Completion
```bash
# Identify conflict
$ ls ~/.zsh-completions/_fabric /usr/local/share/zsh/site-functions/_fabric

# Remove broken user completion
$ rm ~/.zsh-completions/_fabric

# Reload completion
exec zsh
# Or without restart:
unfunction _fabric 2>/dev/null; autoload -U _fabric
```

### Verify Fix
```bash
# Test completions
fabric -<TAB>        # Show all flags
fabric -p <TAB>      # Complete patterns (first fetch, then cached)
fabric -t <TAB>      # Complete temperature values
```

### Optimal Completion Config (Add to ~/.zshrc)
```bash
# Rebuild cache if .zshrc changed
if [[ ~/.zshrc -nt ~/.zcompdump ]]; then
    compinit
else
    compinit -C  # Fast load from cache
fi
```

## The "Blueprint" (The Why/Logic)

### Why the Error Occurred
| Issue | Cause |
|-------|-------|
| `_describe: invalid argument: fabric_patterns` | Broken completion used `_describe 'command' fabric_patterns` but `fabric_patterns` array didn't exist |
| Wrong file loaded | `~/.zsh-completions/` precedes system path in `$fpath` |
| Sourcing vs autoload | Sourcing completion file runs functions outside completion context |

### Zsh Completion Architecture
```
$fpath order:
1. ~/.zsh-completions/     ← User custom (loaded first)
2. /usr/local/share/zsh/site-functions/  ← System packages
3. /usr/share/zsh/functions/Completion/  ← Zsh builtin

Loading:
1. compinit scans $fpath for _* files
2. First match wins (user overrides system)
2. Functions registered via `zle -N` or `compdef`
```

### Cache Design (5-minute TTL)
```bash
# Cache key: per-command (fabric, fabric-ai)
# TTL: 300 seconds
# Location: ~/.cache/fabric-completion/
# Invalidate: fabric_clear_cache function
```

### Helper Functions (Removed)
| Function | Issue |
|----------|-------|
| `_fabric_temperature` | Used `_describe` with undefined arrays |
| `_fabric_topp` | Same `_describe` conflict |
| `_fabric_penalties` | Same `_describe` conflict |

**Fix:** Reverted to simple `_arguments` format, kept caching.

## The "Deep Dive" (The Technical Root)

### Zsh Completion Flow
```
User presses TAB
    ↓
zle triggers completion widget
    ↓
_widgets[_fabric] called
    ↓
_arguments parses spec
    ↓
Actions: _describe, _files, _values, _call_function
    ↓
Results displayed via compadd
```

### `_describe` vs `_arguments`
```bash
# _describe (high-level, menu)
_describe 'command' fabric_patterns

# _arguments (low-level, spec)
_arguments \
  '(-p --pattern)'{-p,--pattern}'[Pattern]: :_fabric_patterns' \
  '(-t --temperature)'{-t,--temperature}'[Temperature]: :_fabric_temperature'
```

### Autoload vs Source
| Method | Behavior |
|--------|----------|
| `source file` | Executes immediately, runs in current context |
| `autoload -U func` | Marks for lazy load, runs in widget context |
| `compinit` | Scans `$fpath`, registers `_*` functions |

### Correct Reload
```bash
# Wrong (causes errors):
source /usr/local/share/zsh/site-functions/_fabric

# Right (Method 1):
exec zsh

# Right (Method 2):
unfunction _fabric 2>/dev/null; autoload -U _fabric
```

### Debug Commands
```bash
# Show loaded completions
$ zle -l | grep fabric

# Show fpath order
$ echo $fpath

# Check which _fabric loaded
$ whence -v _fabric

# Test completion in isolation
$ _fabric
```

### References
- `man zshzle` — Zsh Line Editor
- `man zshcompsys` — Completion System
- [Zsh Manual: Completion](https://zsh.sourceforge.io/Doc/Release/Completion-System.html)