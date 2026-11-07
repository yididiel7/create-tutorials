LOG: [LEARN] Reference: Package Manager Commands (pacman, yay, npm, bun, cargo)

**Title:** Instruct Command for Package Management
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Instruct-Command-for-Package-Management.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### pacman (Arch Official Repositories)
```bash
# Install multiple packages
$ sudo pacman -S package1 package2 package3

# Install with auto-dependencies
$ sudo pacman -Sy --needed package1 package2

# Query installed package info
$ pacman -Qi package-name

# List files owned by package
$ pacman -Ql package-name

# List all installed packages with locations
$ pacman -Ql
```

### yay (AUR Helper)
```bash
# Install AUR package
$ yay -S package-name

# Query package info
$ yay -Qi package-name

# List files
$ yay -Ql package-name
```

### npm / bun (Node.js)
```bash
# npm: install multiple
$ npm install package1 package2 package3

# npm: global install multiple
$ npm install -g package1 package2 package3

# bun: install (project)
$ bun add package1 package2

# bun: global (workspace)
$ bun install -w package1 package2
```

### cargo (Rust)
```bash
# Install binary
$ cargo install package-name

# List installed binaries
$ cargo install --list

# Update installed binaries
$ cargo install --list | awk '{print $1}' | xargs cargo install

# Dependency tree
$ cargo tree
```

## The "Blueprint" (The Why/Logic)

### Package Manager Roles
| Manager | Scope | Use Case |
|---------|-------|----------|
| pacman | System (official repos) | Core system, maintained packages |
| yay | System (AUR) | Community-maintained, cutting-edge |
| npm/bun | Project (Node.js) | JavaScript/TypeScript dependencies |
| cargo | Project (Rust) | Rust dependencies |

### pacman Flags Explained
- `-S` — sync (install from repos)
- `-y` — refresh databases
- `--needed` — skip already installed
- `-Q` — query local database
- `-l` — list files
- `-i` — detailed info

## The "Deep Dive" (The Technical Root)

### pacman Database
- `/var/lib/pacman/local/` — installed package metadata
- `/var/cache/pacman/pkg/` — downloaded packages

### AUR Safety
```bash
# Always review PKGBUILD before installing
$ yay -G package-name  # Download PKGBUILD
$ vim PKGBUILD         # Inspect
$ makepkg -si          # Build and install
```

### bun vs npm
- bun: faster, built-in bundler, `bun.lockb` lockfile
- npm: mature, `package-lock.json`, wider ecosystem

### References
- `man pacman`, `man yay`
- [Arch Wiki: Pacman](https://wiki.archlinux.org/title/Pacman)
- [Arch Wiki: AUR](https://wiki.archlinux.org/title/Arch_User_Repository)