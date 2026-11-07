LOG: [LEARN] Guide: Install Tails OS to USB with Cryptographic Verification

**Title:** Tails Install On Linux
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Tails_Install_On_Linux.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Linux system (any distro)
- USB stick (8 GB minimum, all data lost)
- Internet connection
- GnuPG installed

### Step 1: Download and Verify Signing Key
```bash
$ wget https://tails.boum.org/tails-signing.key
$ gpg --import < tails-signing.key
```

### Step 2: Verify Key via Web of Trust (Debian)
```bash
# Install Debian keyring (contains developer keys)
$ sudo apt update && sudo apt install debian-keyring
# Or on Arch:
$ sudo pacman -S archlinux-keyring

# Import Chris Lamb's key (former Debian PL)
$ gpg --keyring=/usr/share/keyrings/debian-keyring.gpg \
    --export chris@chris-lamb.co.uk | gpg --import

# Check certifications on Tails key
$ gpg --keyid-format 0xlong --check-sigs A490D0F4D311A4153E2BB7CADBB802B258ACD84F
# Look for: sig! 0x1E953E27D4311E58 2020-03-19 Chris Lamb
```

### Step 3: Certify Tails Key with Your Key
```bash
$ gpg --lsign-key A490D0F4D311A4153E2BB7CADBB802B258ACD84F
```

### Step 4: Download Tails USB Image
```bash
# Check latest version at https://tails.boum.org/install/
$ wget --continue https://download.tails.net/tails/stable/tails-amd64-6.11/tails-amd64-6.11.img
```

### Step 5: Verify Image Signature
```bash
$ wget https://tails.boum.org/torrents/files/tails-amd64-6.11.img.sig
$ TZ=UTC gpg --no-options --keyid-format long \
    --verify tails-amd64-6.11.img.sig tails-amd64-6.11.img

# Expected output:
# gpg: Good signature from "Tails developers <tails@boum.org>" [full]
```

### Step 6: Identify USB Device
```bash
$ ls -1 /dev/sd?
# Note current devices

# Plug in USB stick
$ ls -1 /dev/sd?
# New device = your USB (e.g., /dev/sdb)
# ⚠️ ALL DATA WILL BE LOST!
```

### Step 7: Write Image to USB
```bash
$ sudo dd if=tails-amd64-6.11.img of=/dev/sdX bs=16M oflag=direct status=progress
# If permission denied:
$ sudo dd if=tails-amd64-6.11.img of=/dev/sdX bs=16M oflag=direct status=progress
```

### Step 8: Verify and Eject
```bash
$ sync
$ sudo eject /dev/sdX
```

## The "Blueprint" (The Why/Logic)

### Why GnuPG Verification?
- Ensures image not tampered (supply chain security)
- Web of Trust: Debian developers certify Tails key
- Your certification = you trust the chain

### Key Concepts
| Concept | Purpose |
|---------|---------|
| `tails-signing.key` | Tails project's signing key |
| `debian-keyring` | Debian developer keys (trust anchors) |
| `.sig` file | Detached signature |
| `sig!` | Valid certification (exclamation = trusted) |

### dd Options Explained
| Option | Meaning |
|--------|---------|
| `bs=16M` | 16 MB blocks (optimal for flash) |
| `oflag=direct` | Bypass page cache (data integrity) |
| `status=progress` | Show transfer progress |

## The "Deep Dive" (The Technical Root)

### Tails Security Model
- Amnesic: no persistence by default
- Tor-only networking
- Based on Debian stable
- Verified boot chain: BIOS → GRUB → kernel → initramfs

### Signature Verification Details
```bash
# Full verification command breakdown
TZ=UTC                          # UTC timezone for reproducible timestamps
gpg --no-options                # Ignore gpg.conf
    --keyid-format long         # Full key IDs
    --verify sig_file img_file  # Verify detached signature
```

### Alternative: Tails Installer (GUI)
```bash
# On Debian/Ubuntu/Fedora:
$ sudo apt install tails-installer
# Or download AppImage from tails.boum.org
```

### Persistence (Optional)
After first boot, configure encrypted persistence:
- Applications → Tails → Configure persistent volume
- Stores: WiFi passwords, browser bookmarks, GPG keys, etc.

### References
- [Tails Installation Guide](https://tails.boum.org/install/)
- [Tails OpenPGP Verification](https://tails.boum.org/contribute/design/OpenPGP_verification/)
- `man dd`, `man gpg`