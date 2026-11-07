LOG: [LEARN] Guide: Fabric Clipboard Automation with Wayland & Niri

**Title:** Fabric Clipboard Integration - Complete Solution
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** FABRIC-SOLUTION.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Wayland compositor (Niri, Sway, Hyprland, etc.)
- `wl-clipboard` (`wl-copy`, `wl-paste`)
- Fabric AI installed (`pip install fabric-pattern` or `cargo install fabric`)
- Niri compositor (for hotkeys) or compatible WM

### Installation

#### 1. Shell Functions (Any Terminal)
```bash
# One-time setup
cat >> ~/.zshrc << 'EOF'
pbcopy() { wl-copy "$1"; }
pbpaste() { wl-paste; }
pbfabric() { wl-paste | fabric -c; }
EOF
source ~/.zshrc
```

#### 2. Background Monitor (Auto-start)
```bash
# Install monitor script
chmod +x ~/fabric-clipboard-monitor.sh

# Systemd user service (recommended)
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/fabric-clipboard.service << 'EOF'
[Unit]
Description=Fabric Clipboard Monitor
After=graphical-session.target

[Service]
Type=simple
ExecStart=%h/fabric-clipboard-monitor.sh
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF

systemctl --user enable --now fabric-clipboard.service
```

#### 3. Niri Hotkeys (Optional)
```bash
# Add to ~/.config/niri/config.kdl
hotkey "Mod+Alt+C" { exec "pbfabric"; }
hotkey "Mod+Alt+U" { exec "wl-paste -selection primary | fabric -c"; }
hotkey "Mod+Alt+J" { exec "fabric-start"; }
hotkey "Mod+Alt+M" { exec "fabric-stop"; }
```

### Usage Scenarios

#### Scenario 1: Automatic Background Monitoring
```bash
# Start monitor (or enable systemd service)
fabric-clipboard
# Monitors clipboard, processes new content, logs to ~/.fabric-clipboard.log
```

#### Scenario 2: Development/Testing Mode
```bash
fabric-clipboard-dev  # Foreground with visible output, Ctrl+C to stop
```

#### Scenario 3: One-Shot Processing
```bash
fabric-process  # Process current clipboard once, exit
```

#### Scenario 4: Manual Control
```bash
fabric-start   # Start monitoring
fabric-status  # Check if running
fabric-stop    # Stop monitoring
```

#### Niri Hotkeys (Mod+Alt+...)
| Key | Action |
|-----|--------|
| Mod+Alt+C | Process clipboard with Fabric |
| Mod+Alt+U | Process primary selection with Fabric |
| Mod+Alt+J | Start Fabric monitor |
| Mod+Alt+M | Stop Fabric monitor |

### Advanced Patterns
```bash
# Specific pattern
wl-paste | fabric -p summarize

# Custom model
wl-paste | fabric -c --model claude-3-opus

# Multiple patterns
wl-paste | fabric -p summarize -p extract_key_points
```

## The "Blueprint" (The Why/Logic)

### Architecture
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Wayland    │────▶│  wl-paste    │────▶│  Fabric AI  │
│  Clipboard  │     │  (stdout)    │     │  Processing │
└─────────────┘     └──────────────┘     └──────┬──────┘
                                                │
                                                ▼
                                         ┌─────────────┐
                                         │  Terminal/  │
                                         │  Notification│
                                         └─────────────┘
```

### Component Roles
| Component | Purpose |
|-----------|---------|
| `wl-copy`/`wl-paste` | Wayland clipboard I/O |
| `fabric-clipboard-monitor.sh` | Polls clipboard, deduplicates, calls Fabric |
| `fabric -c` | Process stdin with default pattern |
| `fabric -p <pattern>` | Use specific pattern |
| Systemd service | Auto-start, restart on crash |

### Why Polling (Not inotify)?
- Wayland clipboard has no filesystem path
- `wl-paste` is the only interface
- Polling interval (2s default) balances latency vs CPU
- Deduplication via content hash prevents re-processing

## The "Deep Dive" (The Technical Root)

### Monitor Script Internals
```bash
#!/bin/bash
# ~/fabric-clipboard-monitor.sh
LAST_HASH=""
while true; do
    CONTENT=$(wl-paste 2>/dev/null)
    HASH=$(echo -n "$CONTENT" | sha256sum | cut -d' ' -f1)
    if [[ "$HASH" != "$LAST_HASH" && -n "$CONTENT" ]]; then
        echo "$CONTENT" | fabric -c
        LAST_HASH="$HASH"
        echo "$(date): Processed" >> ~/.fabric-clipboard.log
    fi
    sleep "${SLEEP_INTERVAL:-2}"
done
```

### PID File Locking
```bash
PIDFILE=~/.fabric-clipboard.pid
if [[ -f $PIDFILE ]] && kill -0 $(cat $PIDFILE) 2>/dev/null; then
    echo "Already running"
    exit 1
fi
echo $$ > $PIDFILE
trap "rm -f $PIDFILE" EXIT
```

### Systemd Service Details
```ini
[Unit]
Description=Fabric Clipboard Monitor
After=graphical-session.target

[Service]
Type=simple
ExecStart=%h/fabric-clipboard-monitor.sh
Restart=always
RestartSec=5
Environment=DISPLAY=:0
Environment=WAYLAND_DISPLAY=wayland-0

[Install]
WantedBy=default.target
```

### Troubleshooting
| Issue | Fix |
|-------|-----|
| Fabric not found | `which fabric` → `pip install fabric-pattern` |
| wl-copy fails | Check Wayland: `echo $WAYLAND_DISPLAY` |
| Multiple instances | `fabric-stop && rm ~/.fabric-clipboard.pid` |
| Permissions | `chmod +x ~/fabric-clipboard-monitor.sh` |

### Logs
```bash
tail -f ~/.fabric-clipboard.log
grep "error\|failed" ~/.fabric-clipboard.log
```

### Security
- Logs contain first 50 chars of clipboard
- Encrypt logs for sensitive work: `gpg -c ~/.fabric-clipboard.log`
- Set `MAX_CONTENT_LENGTH` to limit processing

### WM Integration
```bash
# i3/Sway
bindsym $mod+Ctrl+f exec fabric-process

# Hyprland
bind = SUPER, ALT, F, exec, fabric-process

# KDE/GNOME: Custom shortcut → `fabric-process`
```

### References
- [Fabric GitHub](https://github.com/danielmiessler/fabric)
- [wl-clipboard](https://github.com/bugaevc/wl-clipboard)
- [Niri Config](https://github.com/YaLTeR/niri)
- `man wl-copy`, `man wl-paste`