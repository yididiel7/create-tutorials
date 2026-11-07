LOG: [LEARN] Guide: Build Custom Arch Linux ISO with archiso

**Title:** archiso Build and Install
**Date:** 2025-12-08 (00:00:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** archiso_build_install.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux installed
- Root/sudo access
- Internet connection

### Step 1: Install archiso
```bash
$ sudo pacman -Syu
$ sudo pacman -S archiso
```

### Step 2: Create Working Directory
```bash
$ mkdir -p ~/archiso-custom
$ cd ~/archiso-custom
```

### Step 3: Copy Default Configuration
```bash
$ cp -r /usr/share/archiso/configs/releng/* ~/archiso-custom/
```

### Step 4: Customize the ISO
Edit configuration files as needed:
- `packages.x86_64` — add/remove packages
- `airootfs/` — customize root filesystem
- `build.sh` — modify build options
- `syslinux/` or `grub/` — bootloader config

### Step 5: Build the ISO
```bash
$ sudo ./build.sh -v
```
ISO output in `out/` directory.

### Step 6: Test the ISO
```bash
$ qemu-system-x86_64 -cdrom out/archlinux-*.iso
```

## The "Blueprint" (The Why/Logic)

### archiso Structure
- `/usr/share/archiso/configs/releng/` — default profile
- `packages.x86_64` — package list for x86_64
- `airootfs/` — becomes `/` in live environment
- `build.sh` — wrapper around `mkarchiso`

### Profiles
- `releng` — official installation media
- `baseline` — minimal base
- Custom profiles in `~/.config/archiso/`

## The "Deep Dive" (The Technical Root)

### Key Directories
| Path | Purpose |
|------|---------|
| `/usr/share/archiso/` | Templates, scripts, hooks |
| `/usr/share/doc/archiso/` | Documentation |
| `/etc/archiso/` | System-wide config |

### Build Process
1. `mkarchiso` creates chroot
2. Installs packages from `packages.x86_64`
3. Applies `airootfs` overlay
4. Generates initramfs with `mkinitcpio`
5. Creates bootable ISO with syslinux/grub

### Customization Examples
```bash
# Add graphical environment
echo "plasma" >> packages.x86_64

# Add custom script
mkdir -p airootfs/usr/local/bin
cp myscript.sh airootfs/usr/local/bin/
chmod +x airootfs/usr/local/bin/myscript.sh
```

### References
- [Arch Wiki: archiso](https://wiki.archlinux.org/title/Archiso)
- `man mkarchiso`
- `man archiso`