LOG: [LEARN] Guide: Handle .pacnew Files on Arch Linux

**Title:** The Warning Message Understand Pacnew
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** The-Warning-Message-Understand-pacnew.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### When You See This Warning
```
warning: /etc/locale.gen installed as /etc/locale.gen.pacnew
```
A new version of a config file was packaged, but your modified version was kept.

### Step 1: Review the .pacnew File
```bash
$ vim /etc/locale.gen.pacnew
# or
$ cat /etc/locale.gen.pacnew
```

### Step 2: Compare with Current Config
```bash
$ diff -u /etc/locale.gen /etc/locale.gen.pacnew
# Or side-by-side:
$ vimdiff /etc/locale.gen /etc/locale.gen.pacnew
```

### Step 3: Merge Changes
```bash
$ vim /etc/locale.gen
# Manually add new lines from .pacnew
# Uncomment required locales (e.g., en_US.UTF-8 UTF-8)
```

### Step 4: Generate Locales
```bash
$ sudo locale-gen
```

### Step 5: Clean Up
```bash
$ sudo rm /etc/locale.gen.pacnew
```

### Automated Tool: pacdiff
```bash
$ sudo pacman -S pacutils
$ sudo pacdiff
# Interactively merge each .pacnew/.pacsave
```

## The "Blueprint" (The Why/Logic)

### Why .pacnew Files Exist
- Pacman never overwrites user-modified config files
- New upstream config saved as `.pacnew`
- You must manually merge changes

### File Types
| Extension | Meaning |
|-----------|---------|
| `.pacnew` | New default config (you modified original) |
| `.pacsave` | Backup of removed config (package removed) |
| `.pacorig` | Original config (from pacman -U downgrade) |

### Merge Strategy
1. **New options** — add them (usually safe)
2. **Changed defaults** — evaluate if you want new behavior
3. **Your customizations** — keep them

## The "Deep Dive" (The Technical Root)

### pacdiff Workflow
```bash
$ pacdiff
# For each file:
#   v — view diff (vimdiff)
#   e — edit current (merge manually)
#   r — replace with .pacnew (lose customizations)
#   q — quit
```

### Configuration File Locations
```
/etc/                    # System configs
/usr/share/pkgname/      # Package defaults (reference)
```

### Finding All .pacnew Files
```bash
$ find /etc -name "*.pacnew" -type f
$ pacman -Qii | grep -A1 "Modified"  # Shows modified configs per package
```

### References
- `man pacman`, `man pacdiff`
- [Arch Wiki: Pacnew and Pacsave](https://wiki.archlinux.org/title/Pacnew_and_Pacsave)
- [Arch Wiki: Configuration files](https://wiki.archlinux.org/title/Configuration_files)