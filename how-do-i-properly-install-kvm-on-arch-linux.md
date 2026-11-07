LOG: [LEARN] Guide: Install KVM/QEMU/libvirt on Arch Linux

**Title:** How to Properly Install KVM on Arch Linux
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** how-do-i-properly-install-kvm-on-arch-linux.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details
**Source:** Adapted from sysguides.com/install-kvm-on-linux

## The "Recipe" (The How)

### Prerequisites
- Arch Linux installed
- CPU with hardware virtualization (Intel VT-x or AMD-V)
- Root/sudo access

### Step 1: Verify Hardware Support
```bash
$ lscpu | grep Virtualization
# Output: VT-x (Intel) or AMD-V (AMD)

$ zgrep CONFIG_KVM /proc/config.gz
# Ensure CONFIG_KVM=m or y
```

### Step 2: Install Packages
```bash
$ sudo pacman -S qemu-full libvirt virt-install virt-manager virt-viewer \
    edk2-ovmf swtpm qemu-img guestfs-tools libosinfo
$ yay -S tuned  # Optional: from AUR
```

### Step 3: Enable Modular libvirt Daemons
```bash
$ for drv in qemu interface network nodedev nwfilter secret storage; do
    sudo systemctl enable virt${drv}d.service
    sudo systemctl enable virt${drv}d{,-ro,-admin}.socket
  done
```

### Step 4: Configure Network Bridge (Optional)
```bash
$ sudo nmcli connection add type bridge con-name bridge0 ifname bridge0
$ sudo nmcli connection add type ethernet slave-type bridge \
    con-name "Bridge connection 1" ifname enp2s0 master bridge0
$ sudo nmcli connection up bridge0
```

### Step 5: Add User to libvirt Group
```bash
$ sudo usermod -aG libvirt $USER
$ echo "export LIBVIRT_DEFAULT_URI='qemu:///system'" >> ~/.bashrc
$ source ~/.bashrc
```

### Step 6: Set ACL on Images Directory
```bash
$ sudo setfacl -R -b /var/lib/libvirt/images
$ sudo setfacl -R -m u:$USER:rwX /var/lib/libvirt/images
$ sudo setfacl -m d:u:$USER:rwx /var/lib/libvirt/images
```

### Step 7: Reboot and Validate
```bash
$ sudo reboot
$ sudo virt-host-validate qemu
```

## The "Blueprint" (The Why/Logic)

### KVM Architecture
- **KVM kernel modules** (`kvm`, `kvm_intel`/`kvm_amd`): Hardware virtualization
- **QEMU** (`qemu-full`): Device emulation, user-space
- **libvirt** (`libvirt`, `virt-install`, `virsh`): Management API/daemon

### Modular vs Monolithic libvirt
- Modular (Arch/Fedora): Separate daemons per driver → granular control
- Monolithic (Ubuntu/Debian): Single `libvirtd` → simpler but less flexible

### Why virtio Drivers?
Para-virtualized drivers for network/disk → near-native performance in guests.

## The "Deep Dive" (The Technical Root)

### IOMMU/VT-d for PCI Passthrough
```bash
# Intel: /etc/default/grub
GRUB_CMDLINE_LINUX="... intel_iommu=on iommu=pt"
$ sudo grub-mkconfig -o /boot/grub/grub.cfg

# Verify
$ dmesg | grep -i -e DMAR -e IOMMU
```

### TuneD Profiles
```bash
$ sudo systemctl enable --now tuned
$ sudo tuned-adm profile virtual-host
$ sudo tuned-adm verify
```

### AMD SEV (Secure Encrypted Virtualization)
```bash
$ lscpu | grep sev
# Enable in BIOS + kernel if supported
```

### References
- [Arch Wiki: KVM](https://wiki.archlinux.org/title/KVM)
- [Arch Wiki: libvirt](https://wiki.archlinux.org/title/Libvirt)
- [sysguides.com](https://sysguides.com/install-kvm-on-linux)