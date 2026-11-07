LOG: [LEARN] Guide: Fix zle _expand_history Error in Zsh

**Title:** Zle Expand History Error Fix
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** zle _expand_history_error_fix.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Problem
```
zle: _expand_history: no such widget
```
Error when using `bindkey ' ' magic-space` with custom magic-space function calling `zle _expand_history`.

### Root Cause
- `_expand_history` is not a standard Zsh widget
- `zshcontrib` module (which provides `magic-space`) not installed on Arch Linux

### Fix: Custom magic-space Widget
```bash
# Add to ~/.zshrc
magic-space() {
    # Expand history (like !!, !$, etc.)
    zle _expand_history
    # Insert space
    zle self-insert
}
zle -N magic-space
bindkey ' ' magic-space
```

### If _expand_history Still Fails
```bash
magic-space() {
    # Use history-expand-word (standard widget)
    zle history-expand-word
    zle self-insert
}
zle -N magic-space
bindkey ' ' magic-space
```

### Test It Works
```bash
$ source ~/.zshrc
$ echo "hello world"
$ !!<SPACE>   # Expands to: echo "hello world"
$ !$<SPACE>   # Expands to: "hello world"
```

## The "Blueprint" (The Why/Logic)

### Why _expand_history Missing
- Part of `zshcontrib` module
- Not included in standard Arch `zsh` package
- Module file: `/usr/lib/zsh/5.9/zshcontrib.so` missing

### Widget Architecture
```bash
# Built-in widgets
zle -l

# Custom widget
my-widget() { zle some-action }
zle -N my-widget
bindkey 'KEY' my-widget
```

### History Expansion Widgets
| Widget | Purpose |
|--------|---------|
| `history-expand-word` | Expand !!, !$, etc. |
| `magic-space` | Expand + insert space |
| `expand-history-or-space` | Combined (if available) |

## The "Deep Dive" (The Technical Root)

### Zsh Line Editor (ZLE)
```
Keystrokes → ZLE → Widget → Action
     ↑          ↑
   bindkey   zle -N
```

### Custom Widget Flow
```bash
magic-space() {
    zle history-expand-word  # Expand !!, !$, !n
    zle self-insert          # Insert space char
}
zle -N magic-space           # Register widget
bindkey ' ' magic-space      # Bind to space
```

### Available Expansion Widgets
```bash
$ zle -l | grep -i expand
# history-expand-word
# expand-history-or-space (if available)
```

### References
- `man zshzle`
- [Zsh Manual: History Expansion](https://zsh.sourceforge.io/Doc/Release/History-Expansion.html)
- [Arch Wiki: Zsh](https://wiki.archlinux.org/title/Zsh)
