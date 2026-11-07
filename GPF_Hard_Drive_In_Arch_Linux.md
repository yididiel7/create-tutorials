LOG: [LEARN] Guide: Partition, Format, and Mount Hard Drive on Arch Linux

**Title:** GPF Hard Drive In Arch Linux
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** GPF_Hard_Drive_In_Arch_Linux.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux live environment or installed system
- Target disk identified (backup data first!)
- Root/sudo access

### Step 1: Identify Target Disk
```bash
$ lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
# Find target: /dev/sdX (e.g., /dev/sdb)
```

### Step 2: Partition with cfdisk
```bash
$ sudo cfdisk /dev/sdX
# Navigate: arrow keys, [New], [Type], [Write], [Quit]
# Create partitions as needed
```

### Step 3: Format Partitions
```bash
# ext4 (recommended for Linux)
$ sudo mkfs.ext4 /dev/sdX1

# xfs (alternative)
$ sudo mkfs.xfs /dev/sdX1

# swap
$ sudo mkswap /dev/sdX2
```

### Step 4: Mount Filesystem
```bash
$ sudo mkdir -p /mnt/mydrive
$ sudo mount /dev/sdX1 /mnt/mydrive
```

### Step 5: Verify Mount
```bash
$ df -h /mnt/mydrive
$ findmnt /mnt/mydrive
```

### Step 6: Persistent Mount (fstab)
```bash
$ sudo blkid /dev/sdX1
# Copy UUID
$ sudo vim /etc/fstab
# Add:
# UUID=xxxx-xxxx  /mnt/mydrive  ext4  defaults  0  2
```

## The "Blueprint" (The Why/Logic)

### Disk vs Partition
- `/dev/sdX` — entire disk (cfdisk target)
- `/dev/sdX1` — partition (format/mount target)

### Filesystem Choice
| FS | Use Case |
|----|----------|
| ext4 | General purpose, Linux native |
| xfs | Large files, high performance |
| btrfs | Snapshots, compression |
| swap | Memory overflow |

### Partition Table
- GPT — modern, >2TB, UEFI
- MBR — legacy, BIOS compatibility

## The "Deep Dive" (The Technical Root)

### cfdisk Workflow
```
cfdisk /dev/sdX
  [New] → size → [Primary/Logical] → [Type] → Linux filesystem (83)
  [Write] → type "yes" → [Quit]
```

### mkfs Details
```bash
# ext4 with label
$ sudo mkfs.ext4 -L mylabel /dev/sdX1

# Check filesystem
$ sudo fsck.ext4 /dev/sdX1

# Tune parameters
$ sudo tune2fs -l /dev/sdX1
```

### fstab Options
```
UUID=xxxx  /mountpoint  fstype  options  dump  pass
```
- `defaults` — rw, suid, dev, exec, auto, nouser, async
- `noatime` — don't update access time (SSD optimization)
- `discard` — TRIM for SSD (or use `fstrim.timer`)

### References
- `man cfdisk`, `man mkfs`, `man fstab`
- [Arch Wiki: Partitioning](https://wiki.archlinux.org/title/Partitioning)
- [Arch Wiki: File systems](https://wiki.archlinux.org/title/File_systems)