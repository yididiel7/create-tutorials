LOG: [LEARN] Reference: Pacman Package Installation Commands

**Title:** Powerful Command-Line Installation Commands
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Powerful-Command-line-Installation-Commands.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Basic Package Install
```bash
$ sudo pacman -S package_name
```

### Multiple Packages
```bash
$ sudo pacman -S package1 package2 package3
```

### Install Without Confirmation
```bash
$ sudo pacman -S --noconfirm package_name
```

### Overwrite Conflicting Files
```bash
$ sudo pacman -S --overwrite '*' package_name
```

### Refresh Databases and Install
```bash
$ sudo pacman -Sy package_name
```

### Install Only If Not Present
```bash
$ sudo pacman -S --needed package_name
```

### Full Upgrade Then Install
```bash
$ sudo pacman -Syu package_name
```

## The "Blueprint" (The Why/Logic)

### Common Flag Combinations
| Flags | Use Case |
|-------|----------|
| `-S` | Sync (install from repo) |
| `-Sy` | Refresh DB + install |
| `-Syu` | Full upgrade + install |
| `--needed` | Skip already installed |
| `--noconfirm` | Automation/scripts |
| `--overwrite '*'` | Force file conflicts |

### Package Groups
```bash
$ sudo pacman -S gnome              # Group
$ sudo pacman -Sg                   # List groups
$ sudo pacman -Qg gnome             # List group packages
```

## The "Deep Dive" (The Technical Root)

### pacman Internals
- Downloads to `/var/cache/pacman/pkg/`
- Extracts to `/` with `libarchive`
- Runs install scripts (pre/post)
- Updates local DB in `/var/lib/pacman/local/`

### Conflict Resolution
```bash
# Check what would be overwritten
$ sudo pacman -S --overwrite '*' --print-format "%f" package

# Manual resolution
$ sudo pacman -Qo /path/to/file
$ sudo pacman -R conflicting-package
```

### References
- `man pacman`
- [Arch Wiki: Pacman](https://wiki.archlinux.org/title/Pacman)