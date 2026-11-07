LOG: [LEARN] Reference: Tmux Display Popup Custom Configuration

**Title:** Tmux Display Popup Custom Configuration
**Date:** 2026-02-14 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Tmux-display-popup-custom-configuration.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Tmux 3.2+ (for `display-popup`)
- TPM (Tmux Plugin Manager) for plugins

### Core Popup Bindings
```bash
# ~/.tmux.conf

# LazyGit popup (Ctrl+Y)
bind C-y display-popup \
  -d "#{pane_current_path}" \
  -w 80% \
  -h 80% \
  -E "lazygit"

# New session popup (Ctrl+N)
bind C-n display-popup -E \
  'bash -i -c "read -p \"Session name: \" name; tmux new-session -d -s \$name && tmux switch-client -t \$name"'

# Session switcher with fzf (Ctrl+J)
bind C-j display-popup -E \
  "tmux list-sessions | sed -E 's/:.*$//' | grep -v \"^$(tmux display-message -p '#S')\$\" | fzf --reverse | xargs tmux switch-client -t"

# IPython popup (Ctrl+P)
bind C-p display-popup -E "ipython"

# rmpc (music) popup (Ctrl+F)
bind C-f display-popup \
  -w 80% \
  -h 80% \
  -E 'rmpc'

# Ranger file manager (Ctrl+R)
bind C-r display-popup \
  -d "#{pane_current_path}" \
  -w 90% \
  -h 90% \
  -E "ranger"

# Edit zshrc (Ctrl+Z)
bind C-z display-popup \
  -w 80% \
  -h 80% \
  -E 'nvim ~/.zshrc'

# Chat script (Ctrl+G)
bind C-g display-popup -E "bash -i ~/.tmux/scripts/chat-popup.sh"

# New zsh pane (Ctrl+T)
bind C-t display-popup \
  -d "#{pane_current_path}" \
  -w 75% \
  -h 75% \
  -E "zsh"
```

### Display Menu (Prefix+D)
```bash
bind d display-menu -T "#[align=centre]Dotfiles" -x C -y C \
  ".zshrc"            z  "display-popup -E 'nvim ~/.zshrc'" \
  ".tmux.conf"        t  "display-popup -E 'nvim ~/.tmux.conf'" \
  ".sketchybarrc"     s  "display-popup -d \"~/.config/sketchybar\" -E 'nvim ~/.config/sketchybar/sketchybarrc'" \
  "Exit"              q  ""
```

### Plugin Configuration (Catppuccin)
```bash
# TPM plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'dreamsofcode-io/catppuccin-tmux'

# Catppuccin theme config
set -g @catppuccin_window_left_separator ""
set -g @catppuccin_window_right_separator " "
set -g @catppuccin_window_middle_separator " █"
set -g @catppuccin_window_number_position "right"
set -g @catppuccin_window_default_fill "number"
set -g @catppuccin_window_default_text "#W"
set -g @catppuccin_window_current_fill "number"
set -g @catppuccin_window_current_text "#W#{?window_zoomed_flag,(),}"

set -g @catppuccin_status_modules_right "directory date_time"
set -g @catppuccin_status_modules_left "session"
set -g @catppuccin_status_left_separator " "
set -g @catppuccin_status_right_separator " "
set -g @catppuccin_status_right_separator_inverse "no"
set -g @catppuccin_status_fill "icon"
set -g @catppuccin_status_connect_separator "no"
set -g @catppuccin_directory_text "#{b:pane_current_path}"
set -g @catppuccin_date_time_text "%H:%M"
set -g @catppuccin_window_status_style "rounded"

set -g status-position top
```

### Split Preserving Path
```bash
bind '%' split-window -h -c "#{pane_current_path}"
bind '"' split-window -v -c "#{pane_current_path}"
```

### Initialize TPM (Bottom of Config)
```bash
run '~/.tmux/plugins/tpm/tpm'
```

## The "Blueprint" (The Why/Logic)

### display-popup Options
| Option | Description |
|--------|-------------|
| `-d PATH` | Working directory |
| `-w WIDTH` | Width (%, px, or cells) |
| `-h HEIGHT` | Height |
| `-E CMD` | Execute command (exits on cmd exit) |
| `-B` | Run in background |
| `-T TITLE` | Popup title |
| `-x/-y` | X/Y position (C=center, R=right, P=pane) |

### Popup vs Split
| Use Case | Method |
|----------|--------|
| Temporary tool (lazygit, ranger) | `display-popup` |
| Persistent workspace | `split-window` |
| Quick REPL (ipython, zsh) | `display-popup -E` |
| Session management | `display-popup` + tmux commands |

### fzf Integration
```bash
# Session switcher with preview
bind C-j display-popup -E \
  "tmux list-sessions -F '#{session_name}: #{session_windows} windows' | \
   fzf --reverse --preview 'tmux capture-pane -pt {}' | \
   cut -d: -f1 | xargs tmux switch-client -t"
```

### Nested Popup Limitation
```bash
# Known issue: nested popups don't work
# Workaround: Use split-window for nested, or redesign
# bind C-k display-popup -E "..."  # May fail if already in popup
```

## The "Deep Dive" (The Technical Root)

### display-popup Internals
- Creates new tmux client attached to popup pane
- Separate from main session pane tree
- Exits when command exits (with `-E`)
- Shares tmux server, separate client

### Environment in Popups
```bash
# Popups inherit most env vars
# But: $TMUX_PANE differs, $TERM may differ
# Use -d for correct working directory
```

### Performance
- Popups create new client → slight overhead
- For frequent use, consider splits instead
- `-B` background mode for long-running

### References
- `man tmux` (DISPLAY-POPUP section)
- [Tmux GitHub](https://github.com/tmux/tmux)
- [Catppuccin Tmux](https://github.com/catppuccin/tmux)