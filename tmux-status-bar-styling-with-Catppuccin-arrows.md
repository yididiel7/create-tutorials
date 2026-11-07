LOG: [LEARN] Reference: Tmux Status Bar with Catppuccin Mocha and Arrow Separators

**Title:** Tmux Status Bar Styling with Catppuccin Arrows
**Date:** 2026-02-01 (19:02:37 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** tmux-status-bar-styling-with-Catppuccin-arrows.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Tmux 3.2+
- Nerd Font (for icons:      )
- Catppuccin Tmux plugin (optional, or manual config)

### Option 1: Manual Config (No Plugin)
```bash
# ~/.tmux.conf

# Catppuccin Mocha Colors
set -g @thm_bg "#1e1e2e"
set -g @thm_fg "#cdd6f4"
set -g @thm_blue "#89b4fa"
set -g @thm_lavender "#b4befe"
set -g @thm_green "#a6e3a1"
set -g @thm_peach "#fab387"
set -g @thm_teal "#94e2d5"
set -g @thm_mauve "#cba6f7"
set -g @thm_mantle "#181825"
set -g @thm_crust "#11111b"
set -g @thm_surface_0 "#313244"
set -g @thm_surface_1 "#45475a"

# Status bar base
set -g status on
set -g status-interval 1
set -g status-justify left
set -g status-position bottom
set -g status-style "fg=#{@thm_fg},bg=#{@thm_mantle}"
set -g status-left-length 80
set -g status-right-length 120

# Left: Hostname with arrows
set -g status-left \
"#[bg=#{@thm_blue},fg=#{@thm_mantle}]\
#[bg=#{@thm_blue},fg=#{@thm_crust},bold] #H \
#[fg=#{@thm_blue},bg=#{@thm_surface_0}]\
#[bg=#{@thm_surface_0},fg=#{@thm_teal}] 󰖶 \
#[fg=#{@thm_surface_0},bg=#{@thm_mantle}]"

# Right: Time, Date, Session with arrows
set -g status-right \
"#[bg=#{@thm_mantle},fg=#{@thm_surface_0}]\
#[bg=#{@thm_surface_0},fg=#{@thm_peach}]  %H:%M \
#[fg=#{@thm_surface_0},bg=#{@thm_mantle}]\
#[bg=#{@thm_surface_0},fg=#{@thm_green}] 󰃭 %Y-%m-%d \
#[fg=#{@thm_surface_0},bg=#{@thm_mantle}]\
#[bg=#{@thm_surface_0},fg=#{@thm_mauve}] 󰅭 #{session_name} \
#[fg=#{@thm_surface_0},bg=#{@thm_mantle}]"

# Window status with arrows
set -g window-status-format \
"#[bg=#{@thm_mantle},fg=#{@thm_surface_1}]\
#[bg=#{@thm_surface_1},fg=#{@thm_subtext_1}] #I #W \
#[bg=#{@thm_mantle},fg=#{@thm_surface_1}]"

set -g window-status-current-format \
"#[bg=#{@thm_mantle},fg=#{@thm_lavender}]\
#[bg=#{@thm_lavender},fg=#{@thm_crust},bold] #I #W \
#[bg=#{@thm_mantle},fg=#{@thm_lavender}]"

# Pane borders
set -g pane-border-style "fg=#{@thm_surface_0}"
set -g pane-active-border-style "fg=#{@thm_lavender}"
```

### Option 2: Catppuccin Tmux Plugin (Recommended)
```bash
# Install plugin (manual)
$ mkdir -p ~/.config/tmux/plugins/catppuccin
$ git clone -b v2.1.3 https://github.com/catppuccin/tmux.git ~/.config/tmux/plugins/catppuccin/tmux

# In ~/.tmux.conf
run ~/.config/tmux/plugins/catppuccin/tmux/catppuccin.tmux

# Configure
set -g @catppuccin_flavor "mocha"
set -g @catppuccin_window_status_style "rounded"

# Custom status modules
set -g status-right-length 100
set -g status-left-length 100
set -g status-left ""
set -g status-right "#{E:@catppuccin_status_application}"
set -agF status-right "#{E:@catppuccin_status_cpu}"
set -ag status-right "#{E:@catppuccin_status_session}"
set -ag status-right "#{E:@catppuccin_status_uptime}"
set -agF status-right "#{E:@catppuccin_status_battery}"

# Load plugin
run ~/.config/tmux/plugins/catppuccin/tmux/catppuccin.tmux
```

### Reload Config
```bash
$ tmux source ~/.tmux.conf
```

## The "Blueprint" (The Why/Logic)

### Arrow Separators
| Symbol | Name | Usage |
|--------|------|-------|
| `` | Left rounded | Start segment |
| `` | Right rounded | End segment |
| `` | Right arrow | Segment transition |
| `` | Left arrow | Reverse transition |
| `` | Left slanted | Alt start |
| `` | Right slanted | Alt end |

### Color Mapping (Catppuccin Mocha)
| Variable | Hex | Use |
|----------|-----|-----|
| `@thm_bg` | #1e1e2e | Base background |
| `@thm_mantle` | #181825 | Status bar bg |
| `@thm_crust` | #11111b | Text on accent |
| `@thm_blue` | #89b4fa | Hostname accent |
| `@thm_lavender` | #b4befe | Active window |
| `@thm_green` | #a6e3a1 | Date |
| `@thm_peach` | #fab387 | Time |
| `@thm_mauve` | #cba6f7 | Session |
| `@thm_teal` | #94e2d5 | Kernel icon |
| `@thm_surface_0` | #313244 | Segment bg |
| `@thm_surface_1` | #45475a | Inactive window |

### Arrow Logic
```
Left side:   Accent  Surface  Mantle
Right side:  Surface  Surface  Mantle
```

## The "Deep Dive" (The Technical Root)

### tmux Format Strings
```bash
#{@variable}       # User-defined variable
#{E:format}        # Expand format string
#[fg=color,bg=color]  # Style override
#I #W              # Window index/name
#{session_name}    # Session name
%H:%M %Y-%m-%d     # strftime
```

### Status Line Structure
```
status-left  | window list | status-right
[left arrows]  [window arrows]  [right arrows]
```

### Powerline Symbols
```bash
# Requires Nerd Font
# Unicode codepoints:
#  U+E0B6   U+E0B4   U+E0B0   U+E0B2
#  U+E0BA   U+E0BC
```

### Plugin Installation
```bash
# Manual (recommended)
$ git clone -b v2.1.3 https://github.com/catppuccin/tmux ~/.config/tmux/plugins/catppuccin

# Or TPM
set -g @plugin 'catppuccin/tmux#v2.1.3'
run '~/.tmux/plugins/tpm/tpm'
```

### Reload & Debug
```bash
$ tmux source ~/.tmux.conf
$ tmux show-options -g status-left
$ tmux show-options -g status-right
```

### References
- [Catppuccin Tmux](https://github.com/catppuccin/tmux)
- [Catppuccin Palette](https://catppuccin.com/palette/)
- `man tmux` (FORMATS section)
