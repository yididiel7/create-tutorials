LOG: [LEARN] Debug: Fix Archcraft Pacman Hook Dependency Errors

**Title:** Updating Archcraft Hooks OS Specific
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Updating-Archcraft-Hooks-OS-Specific.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Error Symptoms
```
error: failed to run hook 'archcraft-hook-zsh.hook'
error: command failed to execute correctly
```
Hooks fail due to missing dependencies.

### Fix: Install Missing Dependencies
```bash
$ sudo pacman -S zsh libnotify --noconfirm --overwrite '*'
```

### Fix: Import and Trust PGP Key (if needed)
```bash
$ sudo pacman-key --recv-keys 19A1E427461B1795F73F629631F4254AFE49E02E
$ sudo pacman-key --lsign-key 19A1E427461B1795F73F629631F4254AFE49E02E
```

### Verify Hooks Work
```bash
$ sudo pacman -Syu
# Watch for hook output:
# Hook #5: "Updating executables in /usr/bin..." — archcraft-hook-zsh.hook
# Hook #6: "Updating Archcraft OS-Specific Configurations..."
# Hook #7: "Updating Archcraft Pixmaps..."
```

## The "Blueprint" (The Why/Logic)

### Archcraft Pacman Hooks
Located in `/usr/share/libalpm/hooks/`:
- `archcraft-hook-zsh.hook` — updates zsh completions
- `archcraft-hook-config.hook` — OS-specific configs
- `archcraft-hook-pixmaps.hook` — icon/theme caches

### Hook Triggers
Run on package transactions matching `Type = Package` and `Operation = Install/Upgrade/Remove`.

### Dependencies
| Hook | Requires |
|------|----------|
| zsh hook | `zsh` |
| config/pixmaps hooks | `libnotify` (for desktop notifications) |

### --overwrite '*'
Forces installation when files conflict between packages. Use cautiously.

## The "Deep Dive" (The Technical Root)

### Hook Format (INI-style)
```ini
[Trigger]
Type = Package
Operation = Install
Operation = Upgrade
Target = *

[Action]
Description = Updating zsh completions...
When = PostTransaction
Exec = /usr/bin/zsh -c "autoload -U compinit; compinit"
```

### PGP Key Trust
- `pacman-key --recv-keys` — fetch from keyserver
- `pacman-key --lsign-key` — locally sign (trust)
- Keys stored in `/etc/pacman.d/gnupg/`

### Debugging Hooks
```bash
# Test hook manually
$ /usr/bin/zsh -c "autoload -U compinit; compinit"

# Verbose pacman
$ sudo pacman -Syu --debug
```

### References
- [Arch Wiki: Pacman Hooks](https://wiki.archlinux.org/title/Pacman#Hooks)
- [Arch Wiki: Pacman-key](https://wiki.archlinux.org/title/Pacman-key)
- Archcraft hooks source: `/usr/share/libalpm/hooks/archcraft-*.hook`