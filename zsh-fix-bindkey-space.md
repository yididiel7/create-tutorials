LOG: [LEARN] Guide: Fix bindkey ' ' magic-space in Zsh

**Title:** Zsh Fix Bindkey Space Magic Space
**Date:** 2026-02-04 (11:25:35 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** zsh-fix-bindkey-space.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Problem
`bindkey ' ' magic-space` doesn't work - space doesn't expand history (`!!`, `!$`, etc.)

### Root Cause
- `magic-space` widget requires `zshcontrib` module
- Module not installed on Arch Linux (`/usr/lib/zsh/5.9/zshcontrib.so` missing)

### Fix: Custom magic-space Widget
```bash
# Add to ~/.zshrc
magic-space() {
    # Expand history (like !!, !$, !:1, etc.)
    zle history-expand-word
    # Insert space
    zle self-insert
}
zle -N magic-space
bindkey ' ' magic-space
```

### Alternative: Use _expand_history
```bash
magic-space() {
    zle _expand_history
    zle self-insert
}
zle -N magic-space
bindkey ' ' magic-space
```

### Test It Works
```bash
$ source ~/.zshrc
$ echo "hello world"
$ !!<SPACE>   # Expands to previous command
$ !$<SPACE>   # Expands to last argument
```

## The "Blueprint" (The Why/Logic)

### Why It Fails on Arch
- `magic-space` is in `zshcontrib` module
- Arch's `zsh` package doesn't include `zshcontrib.so`
- Module file: `/usr/lib/zsh/5.9/zshcontrib.so` missing

### Widget Creation Pattern
```bash
my-widget() {
    zle some-action
    zle another-action
}
zle -N my-widget
bindkey 'KEY' my-widget
```

### Available Expansion Widgets
```bash
$ zle -l | grep -i expand
# history-expand-word (standard)
# expand-history-or-space (if available)
```

## The "Deep Dive" (The Technical Root)

### ZLE Architecture
```
Keystroke → bindkey → Widget → ZLE Action
                ↑
            zle -N
```

### History Expansion Syntax
| Pattern | Expands To |
|---------|------------|
| `!!` | Previous command |
| `!$` | Last argument |
| `!n` | Command n |
| `!-n` | n commands back |
| `!string` | Last command starting with string |

### Zshcontrib Module
```bash
# Check if available
$ ls /usr/lib/zsh/5.9/ | grep contrib

# If missing, use custom widget instead
```

### References
- `man zshzle`
- [Zsh Manual: History Expansion](https://zsh.sourceforge.io/Doc/Release/History-Expansion.html)
- [Arch Wiki: Zsh](https://wiki.archlinux.org/title/Zsh)
