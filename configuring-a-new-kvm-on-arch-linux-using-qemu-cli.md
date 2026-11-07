LOG: [LEARN] Guide: Create KVM Virtual Machine with QEMU CLI on Arch Linux

**Title:** Configuring a New KVM on Arch Linux Using QEMU CLI
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** configuring-a-new-kvm-on-arch-linux-using-qemu-cli.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux with KVM/QEMU installed
- Linux ISO for installation
- Root/sudo access

### Step 1: Create VM Directory
```bash
$ mkdir -p ~/kvm
$ mv /path/to/linux-distro.iso ~/kvm/
$ cd ~/kvm
```

### Step 2: Create Disk Image
```bash
$ qemu-img create -f qcow2 disk.img 20G
```

### Step 3: Install OS (First Boot)
```bash
$ qemu-system-x86_64 \
    -enable-kvm \
    -cdrom linux-distro.iso \
    -boot menu=on \
    -drive file=disk.img,format=qcow2 \
    -m 4G \
    -cpu host \
    -vga virtio \
    -display sdl,gl=on
```

### Step 4: Boot Installed VM
```bash
$ qemu-system-x86_64 \
    -enable-kvm \
    -boot menu=on \
    -drive file=disk.img,format=qcow2 \
    -m 4G \
    -cpu host \
    -vga virtio \
    -display sdl,gl=on
```

## The "Blueprint" (The Why/Logic)

### Key QEMU Options
| Option | Purpose |
|--------|---------|
| `-enable-kvm` | Use KVM acceleration |
| `-cdrom` | Boot from ISO |
| `-boot menu=on` | Show boot menu |
| `-drive file=...,format=qcow2` | Disk image |
| `-m 4G` | 4 GB RAM |
| `-cpu host` | Passthrough host CPU |
| `-vga virtio` | Paravirtualized graphics |
| `-display sdl,gl=on` | SDL with OpenGL |

### qcow2 Format
- Copy-on-write, snapshots, compression
- Native QEMU format, better than raw

## The "Deep Dive" (The Technical Root)

### Advanced Options
```bash
# Multiple cores
-smp 4

# Network (user-mode)
-netdev user,id=net0 -device virtio-net-pci,netdev=net0

# Bridged network (requires bridge setup)
-netdev bridge,id=net0,br=bridge0 -device virtio-net-pci,netdev=net0

# VirtIO disk (better performance)
-drive file=disk.img,if=virtio,format=qcow2

# UEFI boot
-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2-ovmf/x64/OVMF_CODE.fd
-drive if=pflash,format=raw,file=/tmp/OVMF_VARS.fd
```

### Snapshots
```bash
# Create snapshot
$ qemu-img snapshot -c snapshot_name disk.img

# List snapshots
$ qemu-img snapshot -l disk.img

# Apply snapshot
$ qemu-img snapshot -a snapshot_name disk.img
```

### References
- `man qemu-system-x86_64`
- `man qemu-img`
- [Arch Wiki: QEMU](https://wiki.archlinux.org/title/QEMU)