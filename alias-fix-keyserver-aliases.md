LOG: [LEARN] Reference: Fix GPG Keyserver Aliases for Arch Linux

**Title:** Alias Fix Keyserver Aliases
**Date:** 2026-02-02 (20:55:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** alias-fix-keyserver-aliases.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux with pacman
- GPG configured for pacman keys
- Root/sudo access

### Fix 1: Keyserver Auto-Retrieve
```bash
# Add to ~/.zshrc or ~/.bashrc
alias fix-gpg-retrieve="gpg --keyserver-options auto-key-retrieve --receive-keys"
```

### Fix 2: Copy Pacman GPG Config to User Directory
```bash
# Add to ~/.zshrc or ~/.bashrc
alias fix-keyserver='mkdir -p ~/.gnupg && cp /etc/pacman.d/gnupg/gpg.conf ~/.gnupg/ && echo "done"'
```

### Test Aliases
```bash
# Source your config
$ source ~/.zshrc

# Test fix-keyserver
$ fix-keyserver
done

# Test fix-gpg-retrieve (requires a key ID)
$ fix-gpg-retrieve <KEY_ID>
```

## The "Blueprint" (The Why/Logic)

### Why These Fixes Work
| Issue | Root Cause | Solution |
|-------|------------|----------|
| `fix-keyserver` | User `~/.gnupg/gpg.conf` missing or outdated | Copy system pacman GPG config |
| `fix-gpg-retrieve` | Keyserver not configured for auto-retrieve | Add `--keyserver-options auto-key-retrieve` |

### Pacman GPG Key Management
- System keys: `/etc/pacman.d/gnupg/` (managed by pacman)
- User keys: `~/.gnupg/` (used by gpg commands)
- Keyserver pool: `hkps://keyserver.ubuntu.com`, `hkps://keys.openpgp.org`

## The "Deep Dive" (The Technical Root)

### GPG Config Files
```bash
# System (pacman)
/etc/pacman.d/gnupg/gpg.conf
/etc/pacman.d/gnupg/pubring.kbx

# User
~/.gnupg/gpg.conf
~/.gnupg/pubring.kbx
```

### Key Retrieval Flow
```bash
# With auto-key-retrieve
$ gpg --keyserver-options auto-key-retrieve --receive-keys KEYID
# 1. Queries keyserver pool
# 2. Downloads and imports key
# 3. Verifies key signature

# Without (manual)
$ gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys KEYID
```

### Troubleshooting
```bash
# List trusted keys
$ pacman-key -l

# Refresh all keys
$ sudo pacman-key --refresh-keys

# Fix corrupted keyring
$ sudo pacman-key --init
$ sudo pacman-key --populate archlinux
```

### References
- [Arch Wiki: Pacman-key](https://wiki.archlinux.org/title/Pacman-key)
- [Arch Wiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)
- `man gpg`, `man pacman-key`