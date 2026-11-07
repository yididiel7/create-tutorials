LOG: [LEARN] Guide: Create Archcraft Bootable USB with dd

**Title:** Create Archcraft Bootable USB
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** create-archcraft-usb.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Linux system (any distro)
- Archcraft ISO downloaded
- USB drive (4 GB minimum)
- Root/sudo access

### Step 1: Identify USB Device
```bash
$ sudo fdisk -l
# Or:
$ lsblk -o NAME,SIZE,MODEL,TRAN
# Find target: /dev/sdX (e.g., /dev/sdb)
# ⚠️ VERIFY: This will DESTROY all data on the device!
```

### Step 2: Write ISO to USB
```bash
$ sudo dd bs=4M if=path/to/archcraft.iso of=/dev/sdX status=progress oflag=sync
```
- `bs=4M` — 4 MB block size (faster)
- `status=progress` — show progress
- `oflag=sync` — ensure data written before completion

### Step 3: Verify Write
```bash
$ sync
$ sudo fdisk -l /dev/sdX
# Should show ISO partitions
```

## The "Blueprint" (The Why/Logic)

### Why dd?
- Universal: available on all Unix-like systems
- Bit-for-bit copy: preserves ISO hybrid MBR/GPT
- Creates both BIOS and UEFI bootable media
- No additional tools needed

### ISO Hybrid Format
Archcraft ISO is a hybrid image:
- MBR partition table for BIOS
- GPT partition table for UEFI
- El Torito boot sector for optical media

### Block Size Considerations
| bs= | Speed | Notes |
|-----|-------|-------|
| 4M | Fast | Recommended default |
| 1M | Slower | More progress updates |
| 64K | Slowest | Maximum compatibility |

## The "Deep Dive" (The Technical Root)

### dd Command Breakdown
```bash
dd if=input_file of=output_device bs=block_size flags
```
- `if=` — input file (ISO)
- `of=` — output device (USB, NOT partition!)
- `bs=` — read/write block size
- `oflag=sync` — synchronous I/O (data integrity)
- `status=progress` — periodic progress reports

### Safety Checks
```bash
# ALWAYS verify before writing
$ lsblk /dev/sdX
# Check: SIZE matches USB, not system disk!

# Dry run (shows what would happen)
$ sudo dd if=archcraft.iso of=/dev/sdX bs=4M count=0 status=progress
```

### Alternative: Ventoy (Multi-ISO)
```bash
# Install Ventoy to USB once
$ sudo ventoy -i /dev/sdX

# Then copy multiple ISOs to USB as files
$ cp archcraft.iso /mnt/ventoy/
$ cp other.iso /mnt/ventoy/
```

### References
- `man dd`
- [Archcraft Wiki: Boot with USB](https://wiki.archcraft.io/docs/boot-iso/boot-with-usb)
- [Arch Wiki: USB flash installation media](https://wiki.archlinux.org/title/USB_flash_installation_media)