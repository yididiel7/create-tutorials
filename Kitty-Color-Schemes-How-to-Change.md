LOG: [LEARN] Guide: Change Kitty Terminal Color Schemes

**Title:** Kitty Color Schemes How to Change
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Kitty-Color-Schemes-How-to-Change.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Kitty terminal installed
- Kitty config at `~/.config/kitty/kitty.conf`

### Method 1: Themes Kitten (Recommended)
```bash
# Interactive theme selector
$ kitten themes
# Navigate with arrows, Enter to apply

# Direct application
$ kitten themes --reload-in=all "Catppuccin-Mocha"
```

### Method 2: Manual Config (Modular)
```bash
# Edit ~/.config/kitty/kitty.conf
# Change include line:
include colors.conf          # Current
# include dank-theme.conf    # Alternative
# include dark-theme.auto.conf  # Another

# Reload without restart
$ kill -USR1 $(pgrep kitty)
# Or: kitty @ load-config
```

### Method 3: Custom Theme File
```bash
# Create ~/.config/kitty/my-theme.conf
background #1a1b26
foreground #c0caf5
selection_background #33467c
cursor #c0caf5
color0 #414868
color1 #f7768e
color2 #9ece6a
# ... color3-color15

# In kitty.conf:
include my-theme.conf
```

### Method 4: Theme Switcher Script
```bash
#!/bin/bash
# ~/.config/kitty/switch-theme.sh
THEME_DIR="$HOME/.config/kitty/themes"
CONFIG_FILE="$HOME/.config/kitty/kitty.conf"

if [ "$1" = "list" ]; then
    ls "$THEME_DIR" | grep '\.conf$'
    exit 0
fi

THEME_FILE="$THEME_DIR/$1.conf"
[ -f "$THEME_FILE" ] || { echo "Theme '$1' not found"; exit 1; }

sed -i "s|^include .*.conf|include themes/$1.conf|" "$CONFIG_FILE"
kill -USR1 $(pgrep kitty)
```
```bash
$ chmod +x ~/.config/kitty/switch-theme.sh
$ ./switch-theme.sh list
$ ./switch-theme.sh dark
```

### Method 5: Remote Control (Instant)
```bash
# Single color change
$ kitty @ set-colors background="#1a1b26"

# Multiple colors
$ kitty @ set-colors background="#1a1b26" foreground="#c0caf5"

# Full theme via remote
$ kitty @ load-config
```

## The "Blueprint" (The Why/Logic)

### Config Structure
```
~/.config/kitty/
├── kitty.conf           # Main config (includes theme)
├── colors.conf          # Active theme
├── my-theme.conf        # Custom theme
├── themes/              # Theme directory
│   ├── catppuccin.conf
│   ├── dracula.conf
│   └── gruvbox.conf
└── switch-theme.sh      # Switcher script
```

### Built-in Themes
Run `kitten themes` to see all. Popular:
- Catppuccin (Latte, Frappé, Macchiato, Mocha)
- Dracula
- Gruvbox (light/dark)
- Monokai
- Solarized (light/dark)

### Reload Mechanisms
| Method | Command | Scope |
|--------|---------|-------|
| Signal | `kill -USR1 $(pgrep kitty)` | All kitty windows |
| Remote | `kitty @ load-config` | Current session |
| Remote | `kitten themes --reload-in=all` | All sessions |

## The "Deep Dive" (The Technical Root)

### Color Palette Format
```bash
# 16-color ANSI palette
color0  # black
color1  # red
color2  # green
color3  # yellow
color4  # blue
color5  # magenta
color6  # cyan
color7  # white
color8  # bright black
color9  # bright red
color10 # bright green
color11 # bright yellow
color12 # bright blue
color13 # bright magenta
color14 # bright cyan
color15 # bright white

# Special colors
background      # default background
foreground      # default foreground
selection_background  # text selection bg
selection_foreground  # text selection fg
cursor          # cursor color
cursor_text_color     # text on cursor
```

### kitty.conf Include Pattern
```bash
# In kitty.conf
include colors.conf
# OR
include themes/catppuccin-mocha.conf
```

### Remote Control Protocol
```bash
# Unix socket at $KITTY_LISTEN_ON
# Requires: allow_remote_control yes in kitty.conf
```

### References
- [Kitty Themes](https://sw.kovidgoyal.net/kitty/conf/#themes)
- [Kitty Remote Control](https://sw.kovidgoyal.net/kitty/remote-control/)
- `kitten themes --help`