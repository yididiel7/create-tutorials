LOG: [LEARN] Guide: Format Hard Drive with fdisk/cfdisk on Arch Linux

**Title:** Formatting a Hard Drive Using fdisk/cfdisk on Arch Linux
**Date:** 2025-11-18 (00:17:22 IST)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Formatting-Hard-Drive-fdisk-cfdisk-Arch-Linux.md
**Copyright:** © 2025-2026 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux system
- Root/sudo access
- Target drive identified

### Required Packages
```bash
sudo pacman -S fdisk parted dosfstools ntfs-3g
```

### Step 1: Identify Target Drive
```bash
# List all drives
sudo fdisk -l

# Simpler view
lsblk
```
**Output example:**
```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda     8:0    0 238.5G  0 disk
├─sda1  8:1    0   512M  0 part /boot
└─sda2  8:2    0   238G  0 part /
sdb     8:16   0   1.8T  0 disk
```

### Step 2: Partition with cfdisk (Beginner-Friendly)
```bash
sudo cfdisk /dev/sdX
```
**In cfdisk:**
| Key | Action |
|-----|--------|
| ↑/↓ | Navigate partitions |
| `New` | Create partition |
| `Primary`/`Logical` | Partition type |
| `Size` | Set partition size |
| `Type` | Filesystem type (83=Linux, 7=NTFS, b=FAT32) |
| `Write` | Apply changes |
| `Quit` | Exit |

### Step 3: Partition with fdisk (Traditional)
```bash
sudo fdisk /dev/sdX
```
**Key commands:**
| Key | Action |
|-----|--------|
| `n` | New partition |
| `d` | Delete partition |
| `t` | Change type (83=Linux, 7=NTFS, b=FAT32) |
| `p` | Print table |
| `w` | Write & exit |
| `q` | Quit without saving |

**Example workflow:**
```
Command (m for help): n
Partition type: p (primary)
Partition number: 1
First sector: [Enter for default]
Last sector: +50G

Command (m for help): t
Selected partition 1
Hex code: 83

Command (m for help): w
```

### Step 4: Format Partition
```bash
# ext4 (Linux)
sudo mkfs.ext4 /dev/sdX1

# FAT32 (cross-platform)
sudo mkfs.fat -F32 /dev/sdX1

# NTFS (Windows compatible)
sudo mkfs.ntfs /dev/sdX1

# Btrfs
sudo mkfs.btrfs /dev/sdX1
```

### Step 5: Mount & Verify
```bash
# Create mount point
sudo mkdir /mnt/mydrive

# Mount
sudo mount /dev/sdX1 /mnt/mydrive

# Verify
df -h
lsblk
```

### Step 8: Auto-mount at Boot (/etc/fstab)
```bash
sudo nano /etc/fstab
```
Add line:
```
/dev/sdX1   /mnt/mydrive   ext4   defaults   0   2
```

## The "Blueprint" (The Why/Logic)

### Tool Comparison
| Tool | Best For | Learning Curve |
|------|----------|----------------|
| `cfdisk` | Beginners, visual | Low |
| `fdisk` | Scripts, automation | Medium |
| `parted` | GPT, large disks, scripts | Medium-High |

### Filesystem Selection
| FS | Use Case | Max Size | Linux | Windows | macOS |
|----|----------|----------|-------|---------|-------|
| ext4 | Linux native | 1 EiB | ✓ | ✗* | ✗* |
| Btrfs | Snapshots, CoW | 16 EiB | ✓ | ✗ | ✗ |
| FAT32 | USB, cross-platform | 2 TiB | ✓ | ✓ | ✓ |
| NTFS | Windows shared | 256 TiB | ✓ | ✓ | ✓* |
| exFAT | Large files, cross-platform | 128 PiB | ✓ | ✓ | ✓ |

*Requires additional software

### Partition Table: MBR vs GPT
| Scheme | Max Partitions | Max Disk | UEFI Boot | Legacy Boot |
|--------|----------------|----------|-----------|-------------|
| MBR | 4 primary | 2 TiB | ✗ | ✓ |
| GPT | 128+ | 9.4 ZiB | ✓ | ✓* |

*Requires BIOS support

## The "Deep Dive" (The Technical Root)

### Block Device Internals
```
/dev/sdX     → Entire disk
/dev/sdX1    → Partition 1
/dev/sdX2    → Partition 2
```

### Filesystem Creation Details
```bash
# ext4 with label
sudo mkfs.ext4 -L "MYDRIVE" /dev/sdX1

# FAT32 with label
sudo mkfs.fat -F32 -n "MYDRIVE" /dev/sdX1

# NTFS with label
sudo mkfs.ntfs -L "MYDRIVE" /dev/sdX1
```

### fstab Fields
```
<device>  <mount>  <fs>  <options>  <dump>  <pass>
/dev/sdX1 /mnt/drive ext4 defaults    0       2
              │       │    │          │       │
              │       │    │          │       └── fsck order (0=skip, 1=root, 2+=check)
              │       │    │          └──────── dump backup (0=ignore)
              │       │    └─────────────────── mount options
              │       └──────────────────────── filesystem type
              └──────────────────────────────── mount point
```

### parted (Scriptable Alternative)
```bash
# GPT + full disk partition
sudo parted /dev/sdX mklabel gpt
sudo parted /dev/sdX mkpart primary ext4 1MiB 100%
```

### Safety Checklist
- [ ] Verify device with `lsblk` and `fdisk -l`
- [ ] Unmount: `sudo umount /dev/sdX*`
- [ ] Backup data first
- [ ] Double-check device path
- [ ] Test mount before fstab

### References
- `man fdisk`, `man cfdisk`, `man mkfs`, `man fstab`
- [Arch Wiki: Partitioning](https://wiki.archlinux.org/title/Partitioning)
- [Arch Wiki: File systems](https://wiki.archlinux.org/title/File_systems)
- [Arch Wiki: fstab](https://wiki.archlinux.org/title/Fstab)