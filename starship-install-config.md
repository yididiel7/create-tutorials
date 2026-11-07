LOG: [LEARN] Guide: Install and Configure Starship Prompt

**Title:** Starship Install Config
**Date:** 2023-12-29
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** starship-install-config.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Rust toolchain (for building) or package manager
- Nerd Font installed (for icons)
- Compatible shell: bash, zsh, fish, nushell, etc.

### Install Starship
```bash
# Arch Linux
$ sudo pacman -S starship

# Universal (Rust)
$ curl -sS https://starship.rs/install.sh | sh

# Other package managers
$ brew install starship      # macOS
$ dnf install starship       # Fedora
$ apt install starship       # Ubuntu/Debian (may be older)
```

### Configure Shell
```bash
# Bash (~/.bashrc)
eval "$(starship init bash)"

# Zsh (~/.zshrc)
eval "$(starship init zsh)"

# Fish (~/.config/fish/config.fish)
starship init fish | source

# Nushell
mkdir -p ~/.config/nushell
echo 'eval (starship init nu)' >> ~/.config/nushell/env.nu
```

### Configure Starship
```bash
# Create config directory
$ mkdir -p ~/.config

# Create config file
$ starship preset nerd-font-symbols -o ~/.config/starship.toml
# Or use blank preset
$ starship preset plain-text-symbols -o ~/.config/starship.toml
```

### Install Nerd Font (Required for Icons)
```bash
# Arch Linux
$ sudo pacman -S nerd-fonts

# Manual: Download from https://www.nerdfonts.com/font-downloads
# Recommended: FiraCode Nerd Font, JetBrainsMono Nerd Font

# Set in terminal emulator (Kitty example)
# font_family FiraCode Nerd Font
```

### Test Installation
```bash
$ starship --version
$ starship explain  # Shows active modules
```

## The "Blueprint" (The Why/Logic)

### Why Starship?
| Feature | Benefit |
|---------|---------|
| Written in Rust | Fast, minimal overhead |
| Cross-shell | Same config for bash/zsh/fish |
| Modular | Enable/disable modules easily |
| No external deps | Just one binary |

### Module System
```toml
# ~/.config/starship.toml
[directory]
truncation_length = 3
truncation_symbol = "…/"

[git_branch]
symbol = "🌱 "

[cmd_duration]
min_time = 500
format = "took [$duration]($style) "
```

### Common Modules
| Module | Shows |
|--------|-------|
| `directory` | Current path |
| `git_branch` | Branch name |
| `git_status` | Dirty/clean state |
| `cmd_duration` | Last command time |
| `python`/`node`/`rust` | Version when in project |
| `docker_context` | Active Docker context |
| `kubernetes` | Current k8s context |

## The "Deep Dive" (The Technical Root)

### Configuration File Structure
```toml
# ~/.config/starship.toml
format = """$all"""

# Prompt order
prompt_order = [
  "username",
  "hostname",
  "directory",
  "git_branch",
  "git_status",
  "cmd_duration",
  "character",
]

# Module config
[character]
success_symbol = "[➜](bold green)"
error_symbol = "[➜](bold red)"
vicmd_symbol = "[❮](bold green)"

[directory]
style = "bold cyan"
truncation_length = 3

[git_branch]
symbol = "🌱 "
style = "bold green"

[git_status]
conflicted = "🏳"
ahead = "⇡${count}"
behind = "⇣${count}"
diverged = "⇕⇡${ahead_count}⇣${behind_count}"
untracked = "?"
stashed = "$"
modified = "!"
deleted = "🗑"
```

### Performance
- Starship written in Rust, minimal overhead
- Lazy module loading (only runs when needed)
- Caching for git operations
- Typical overhead: < 5ms

### Advanced: Custom Commands
```toml
[custom.foo]
command = "echo hello"
when = "true"
format = "[$output]($style) "
```

### References
- [Starship Docs](https://starship.rs/config/)
- [Starship Presets](https://starship.rs/presets/)
- [Nerd Fonts](https://www.nerdfonts.com/)
- `starship --help`, `starship explain`