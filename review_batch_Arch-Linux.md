# Review Batch: Arch-Linux

**Generated:** 2026-11-04
**Files:** 18 (4 P0 tutorials, 14 P1 references)
**Standard:** 4-section format with `LOG: [LEARN]` header + Recipe/Blueprint/Deep Dive + Metadata

---

## Summary of Changes per File

### P0 Tutorials (Full Restructure + Content Verification)

| File | Primary Issues | Restructure Needed |
|------|---------------|-------------------|
| `Beginner_Tutorial_Arch0_Intro_CLI.md` | 17 headers, 22 code blocks, 14 inline spacing, missing metadata, no LOG header | ✅ Full 4-section |
| `Customizing-Your-Linux-System-with-User-Management.md` | 33 headers, 20 code blocks, 9 inline spacing, duplicated content, missing metadata | ✅ Full 4-section |
| `how-do-i-properly-install-kvm-on-arch-linux.md` | 18 line len, 25 headers, 50 code blocks, 20 inline, 11 trailing, missing metadata | ✅ Full 4-section |
| `Instruct-Command-for-Package-Management.md` | 29 code blocks, 24 inline spacing, 1 trailing, missing metadata | ✅ Full 4-section |
| `Install_Setup-and-enable-the_Auditd_service.md` | 1 line len, 2 headers, 7 code blocks, 7 inline, 7 trailing, missing metadata | ✅ Full 4-section |

### P1 References (Structural Fixes + Metadata + LOG Header)

| File | Primary Issues |
|------|---------------|
| `Arch_Linux_command-line_commands.md` | 1 header, 1 code block, 16 inline spacing, **has metadata** but wrong case, no LOG |
| `archiso_build_install.md` | 20 line len, 2 trailing, missing metadata |
| `build-llama.cpp-on-Arch-Linux.md` | Missing metadata only |
| `Check-Locale-Installation-Packages_2026-02-11_20-43-04.md` | 14 headers, 2 code blocks, 9 inline, missing metadata |
| `configuring-a-new-kvm-on-arch-linux-using-qemu-cli.md` | Missing metadata only |
| `Create-a-New-VENV-Installing-UV-on-Archlinux.md` | 1 inline, **has metadata**, no LOG |
| `GPF_Hard_Drive_In_Arch_Linux.md` | 16 line len, 11 headers, 3 inline, missing metadata |
| `Powerful-Command-line-Installation-Commands.md` | 1 code block, missing metadata |
| `SysAdmin-Linux-Commands.md` | Missing metadata only |
| `The-Warning-Message-Understand-pacnew.md` | Missing metadata only |
| `Updating-Archcraft-Hooks-OS-Specific.md` | Missing metadata only |
| `create-archcraft-usb.md` | 5 line len, 3 headers, 1 trailing, missing metadata |
| `Tails_Install_On_Linux.md` | 19 line len, 3 headers, 1 trailing, missing final newline, missing metadata |

---

## Detailed Diffs

### 1. Beginner_Tutorial_Arch0_Intro_CLI.md (P0)

**Issues Found:**
- 17 headers (mixed Setext/ATX, wrong case)
- 22 code blocks missing language tags
- 14 inline code spacing violations
- Missing metadata block (all 6 fields)
- No `LOG: [LEARN]` header
- Content has procedural steps but no conceptual structure

**Content Corrections Needed:**
- `ssh-agent` and `sshd` are not package names (Arch uses `openssh`)
- `useradd -m sshuser` should be `useradd -m -G wheel sshuser` for sudo
- `/etc/init.d/` and `rc.d` are SysVinit — Arch uses systemd only
- `sudo systemctl start ssh` → `sudo systemctl start sshd`
- Duplicate sections at end of file

**Proposed Structure:**
```
LOG: [LEARN] Guide: Beginner Arch Linux CLI Setup

**Title:** Beginner Tutorial: Arch Linux CLI Introduction
**Date:** 2025-11-15 (20:57:02 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Beginner_Tutorial_Arch0_Intro_CLI.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux installed
- Root/sudo access
- Internet connection

### Steps
1. Install required packages
   ```bash
   $ sudo pacman -S curl openssh pwgen
   ```

2. Generate SSH key pair
   ```bash
   $ ssh-keygen -t ed25519 -C "your-email@example.com"
   ```

3. Start and enable sshd service
   ```bash
   $ sudo systemctl enable --now sshd
   ```

4. Configure SSH (optional hardening)
   ```bash
   $ sudo vim /etc/ssh/sshd_config
   # Set: PermitRootLogin no, PasswordAuthentication no
   $ sudo systemctl restart sshd
   ```

## The "Blueprint" (The Why/Logic)

### Why These Packages?
- `curl`: Download files, test APIs
- `openssh`: Provides `sshd` (server), `ssh` (client), `ssh-keygen`, `ssh-agent`
- `pwgen`: Generate secure passwords

### Why ed25519 Over RSA?
- Smaller keys, faster operations, better security
- Modern standard (OpenSSH 6.5+)

### systemd vs SysVinit
Arch Linux uses systemd exclusively. No `/etc/init.d/`, no `rc.d`.

## The "Deep Dive" (The Technical Root)

### SSH Service Details
- Service unit: `/usr/lib/systemd/system/sshd.service`
- Config: `/etc/ssh/sshd_config` (man `sshd_config`)
- Keys stored in `/etc/ssh/` (host) and `~/.ssh/` (user)

### Troubleshooting
- `systemctl status sshd` — check service state
- `journalctl -u sshd` — view logs
- `sshd -t` — test config syntax

### References
- [Arch Wiki: OpenSSH](https://wiki.archlinux.org/title/OpenSSH)
- [Arch Wiki: systemd](https://wiki.archlinux.org/title/systemd)
```

---

### 2. Customizing-Your-Linux-System-with-User-Management.md (P0)

**Issues Found:**
- 33 headers (duplicated sections)
- 20 code blocks missing language tags
- 9 inline code spacing violations
- **Entire content duplicated** (prompt + assistant response repeated twice)
- Missing metadata block
- No `LOG: [LEARN]` header
- Uses `sudo` group — Arch uses `wheel` group

**Content Corrections:**
- Arch uses `wheel` group for sudo, not `sudo` group
- `visudo` edits `/etc/sudoers` — correct
- `/etc/sudoers.d/` — correct
- TinyURL link should be expanded or removed

**Proposed Structure:**
```
LOG: [LEARN] Understanding: Linux User Management and Sudo Privileges

**Title:** Customizing Your Linux System with User Management
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Customizing-Your-Linux-System-with-User-Management.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Linux system with sudo
- Root/sudo access

### Method 1: Add User to wheel Group (Arch Standard)
```bash
# Add existing user to wheel group
$ sudo usermod -aG wheel username
# Verify
$ groups username
```

### Method 2: Edit sudoers with visudo
```bash
$ sudo visudo
# Add line:
username ALL=(ALL:ALL) ALL
# Or passwordless:
username ALL=(ALL:ALL) NOPASSWD:ALL
# Or specific commands:
username ALL=(ALL) /usr/bin/pacman
```

### Method 3: Drop-in File in /etc/sudoers.d/
```bash
$ sudo visudo -f /etc/sudoers.d/username
# Add:
username ALL=(ALL:ALL) ALL
```

### Verify Sudo Access
```bash
$ sudo -l -U username
```

## The "Blueprint" (The Why/Logic)

### Why wheel Group?
Arch Linux follows the traditional BSD convention where `wheel` group members may `su` to root. The default `/etc/sudoers` includes:
```
%wheel ALL=(ALL:ALL) ALL
```

### Why visudo?
- Validates syntax before saving
- Prevents lockout from malformed sudoers
- Uses `EDITOR` environment variable

### Security Principle: Least Privilege
- Grant only needed commands
- Prefer drop-in files (`/etc/sudoers.d/`) for auditability
- Audit regularly: `sudo -l -U username`

## The "Deep Dive" (The Technical Root)

### sudoers Syntax
```
user  host=(runas:runas_group) commands
```

### File Precedence
1. `/etc/sudoers` (main)
2. `/etc/sudoers.d/*` (drop-ins, lexical order)

### Troubleshooting
- `sudo visudo -c` — check syntax
- `groups` — verify current user groups (relogin after changes)
- `sudo -k` — reset timestamp cache

### References
- `man sudoers`, `man visudo`
- [Arch Wiki: Sudo](https://wiki.archlinux.org/title/Sudo)
```

---

### 3. how-do-i-properly-install-kvm-on-arch-linux.md (P0)

**Issues Found:**
- 18 lines >72 cols
- 25 headers (mixed case)
- 50 code blocks missing language tags
- 20 inline spacing violations
- 11 trailing whitespace
- Missing metadata block
- No `LOG: [LEARN]` header
- Content is copied from sysguides.com (needs attribution)
- Multi-distro (Fedora, Ubuntu, Arch) — should focus on Arch

**Content Corrections:**
- Focus on Arch Linux commands only
- `qemu-full` is correct Arch package (not `qemu-kvm`)
- Modular libvirt daemons: `virtqemud`, `virtnetworkd`, etc.
- `grub-mkconfig -o /boot/grub/grub.cfg` for Arch

**Proposed Structure:**
```
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
```

---

### 4. Instruct-Command-for-Package-Management.md (P0)

**Issues Found:**
- 29 code blocks missing language tags
- 24 inline spacing violations
- 1 trailing whitespace
- Missing metadata block
- No `LOG: [LEARN]` header
- Content is AI chat transcript (ollama) — needs restructuring
- Mixes bun, npm, pacman, yay, cargo — should focus per section

**Proposed Structure:**
```
LOG: [LEARN] Reference: Package Manager Commands (pacman, yay, npm, bun, cargo)

**Title:** Instruct Command for Package Management
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Instruct-Command-for-Package-Management.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### pacman (Arch Official Repositories)
```bash
# Install multiple packages
$ sudo pacman -S package1 package2 package3

# Install with auto-dependencies
$ sudo pacman -Sy --needed package1 package2

# Query installed package info
$ pacman -Qi package-name

# List files owned by package
$ pacman -Ql package-name

# List all installed packages with locations
$ pacman -Ql
```

### yay (AUR Helper)
```bash
# Install AUR package
$ yay -S package-name

# Query package info
$ yay -Qi package-name

# List files
$ yay -Ql package-name
```

### npm / bun (Node.js)
```bash
# npm: install multiple
$ npm install package1 package2 package3

# npm: global install multiple
$ npm install -g package1 package2 package3

# bun: install (project)
$ bun add package1 package2

# bun: global (workspace)
$ bun install -w package1 package2
```

### cargo (Rust)
```bash
# Install binary
$ cargo install package-name

# List installed binaries
$ cargo install --list

# Update installed binaries
$ cargo install --list | awk '{print $1}' | xargs cargo install

# Dependency tree
$ cargo tree
```

## The "Blueprint" (The Why/Logic)

### Package Manager Roles
| Manager | Scope | Use Case |
|---------|-------|----------|
| pacman | System (official repos) | Core system, maintained packages |
| yay | System (AUR) | Community-maintained, cutting-edge |
| npm/bun | Project (Node.js) | JavaScript/TypeScript dependencies |
| cargo | Project (Rust) | Rust dependencies |

### pacman Flags Explained
- `-S` — sync (install from repos)
- `-y` — refresh databases
- `--needed` — skip already installed
- `-Q` — query local database
- `-l` — list files
- `-i` — detailed info

## The "Deep Dive" (The Technical Root)

### pacman Database
- `/var/lib/pacman/local/` — installed package metadata
- `/var/cache/pacman/pkg/` — downloaded packages

### AUR Safety
```bash
# Always review PKGBUILD before installing
$ yay -G package-name  # Download PKGBUILD
$ vim PKGBUILD         # Inspect
$ makepkg -si          # Build and install
```

### bun vs npm
- bun: faster, built-in bundler, `bun.lockb` lockfile
- npm: mature, `package-lock.json`, wider ecosystem

### References
- `man pacman`, `man yay`
- [Arch Wiki: Pacman](https://wiki.archlinux.org/title/Pacman)
- [Arch Wiki: AUR](https://wiki.archlinux.org/title/Arch_User_Repository)
```

---

### 5. Install_Setup-and-enable-the_Auditd_service.md (P0)

**Issues Found:**
- 1 line >72 cols
- 2 headers (Setext style)
- 7 code blocks missing language tags
- 7 inline spacing violations
- 7 trailing whitespace
- Missing metadata block
- No `LOG: [LEARN]` header
- **Incorrect commands**: `sudo pacman -U auditd` (should be `-S`), `rc.local` editing (obsolete), malformed `auditd` flags

**Content Corrections:**
- `sudo pacman -S audit` (package name is `audit`, not `auditd`)
- systemd service: `sudo systemctl enable --now auditd`
- Rules in `/etc/audit/rules.d/`
- No `rc.local` on Arch

**Proposed Structure:**
```
LOG: [LEARN] Guide: Install and Configure auditd on Arch Linux

**Title:** Install, Setup, and Enable the Auditd Service
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Install_Setup-and-enable-the_Auditd_service.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux
- Root/sudo access

### Step 1: Install audit Package
```bash
$ sudo pacman -S audit
```

### Step 2: Enable and Start Service
```bash
$ sudo systemctl enable --now auditd
```

### Step 3: Configure Audit Rules
```bash
# Create rules file
$ sudo vim /etc/audit/rules.d/audit.rules

# Example: Monitor file access
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k scope

# Example: Monitor syscalls
-a always,exit -F arch=b64 -S execve -k exec
```

### Step 4: Load Rules and Verify
```bash
$ sudo auditctl -R /etc/audit/rules.d/audit.rules
$ sudo auditctl -l
$ sudo systemctl status auditd
```

### Step 5: View Logs
```bash
$ sudo ausearch -k identity
$ sudo aureport --summary
```

## The "Blueprint" (The Why/Logic)

### auditd Components
- **auditd daemon**: Kernel → userspace log collector
- **auditctl**: Runtime rule management
- **ausearch/aureport**: Log analysis
- **Rules**: `/etc/audit/rules.d/*.rules` (persistent)

### Rule Syntax
```
-w path -p permissions -k keyname    # File watch
-a action,filter -S syscall -k key   # Syscall audit
```

### Permissions
- `r` — read, `w` — write, `x` — execute, `a` — attribute change

## The "Deep Dive" (The Technical Root)

### Kernel Audit Subsystem
- Netlink socket communication
- Kernel ring buffer (configurable size)
- Rate limiting: `auditctl --rate-limit`

### Performance Considerations
- High syscall volume → disk I/O pressure
- Use `-F` filters to reduce noise
- Consider `audispd` plugins for remote logging

### Integration
- `auditd` + `systemd` — automatic service management
- `auditd` + `SELinux` — combined MAC + audit
- Log forwarding: `audispd-plugins` → syslog/remote

### References
- `man auditd`, `man auditctl`, `man ausearch`
- [Arch Wiki: Audit](https://wiki.archlinux.org/title/Audit_framework)
- [Red Hat Audit Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/setting-up-and-configuring-auditing)
```

---

### 6. Arch_Linux_command-line_commands.md (P1)

**Issues Found:**
- 1 header case issue
- 1 code block missing language tag
- 16 inline spacing violations
- **Has metadata block** (but "Command line" → "Command-Line")
- No `LOG: [LEARN]` header
- Content is AI-generated list (two prompts duplicated)
- `memoryinfo` is not a command
- `getconf MCEXTNAME` is obscure

**Proposed Fix:** Add LOG header, fix metadata case, tag code blocks, fix inline spacing, deduplicate.

---

### 7. archiso_build_install.md (P1)

**Issues Found:**
- 20 lines >72 cols
- 2 trailing whitespace
- Missing metadata block
- No `LOG: [LEARN]` header
- Good content, just needs structure

**Proposed Structure:** Add LOG header + metadata, wrap lines, fix trailing whitespace, organize into Recipe/Blueprint/Deep Dive.

---

### 8. build-llama.cpp-on-Arch-Linux.md (P1)

**Issues Found:**
- Missing metadata block only
- No `LOG: [LEARN]` header
- Content is minimal but correct

**Proposed Fix:** Add LOG header + metadata block.

---

### 9. Check-Locale-Installation-Packages_2026-02-11_20-43-04.md (P1)

**Issues Found:**
- 14 headers
- 2 code blocks missing language tags
- 9 inline spacing violations
- Missing metadata block
- No `LOG: [LEARN]` header
- Content is Duck.ai chat transcript (3 prompts)
- Contains Debian commands (`dpkg-reconfigure`, `apt`) mixed with Arch

**Content Corrections:**
- Remove Debian-specific commands
- Focus on Arch: `locale-gen`, `/etc/locale.gen`, `/etc/locale.conf`

---

### 10. configuring-a-new-kvm-on-arch-linux-using-qemu-cli.md (P1)

**Issues Found:**
- Missing metadata block only
- No `LOG: [LEARN]` header
- Minimal but correct QEMU commands

**Proposed Fix:** Add LOG header + metadata, expand with Blueprint/Deep Dive.

---

### 11. Create-a-New-VENV-Installing-UV-on-Archlinux.md (P1)

**Issues Found:**
- 1 inline spacing violation
- **Has metadata block** (complete)
- No `LOG: [LEARN]` header
- Content has duplicated sections (Prompt #1 + Prompt #2)
- `uv create` → `uv venv` (deprecated)
- `uv on`/`uv off` → not standard (use `source .venv/bin/activate`)

**Content Corrections:**
- Update to current `uv` commands
- Deduplicate

---

### 12. GPF_Hard_Drive_In_Arch_Linux.md (P1)

**Issues Found:**
- 16 lines >72 cols
- 11 headers
- 3 inline spacing violations
- Missing metadata block
- No `LOG: [LEARN]` header
- Contains Excel-style table (not Markdown)
- `cfdisk /dev/sdb1` → should be `/dev/sdb` (disk, not partition)

**Content Corrections:**
- Fix device path
- Convert Excel table to Markdown
- `mkfs` needs filesystem type: `mkfs.ext4 /dev/sdX1`

---

### 13. Powerful-Command-line-Installation-Commands.md (P1)

**Issues Found:**
- 1 code block missing language tag
- Missing metadata block
- No `LOG: [LEARN]` header
- Single command only

**Proposed Fix:** Add LOG header + metadata, tag code block, expand with context.

---

### 14. SysAdmin-Linux-Commands.md (P1)

**Issues Found:**
- Missing metadata block only
- No `LOG: [LEARN]` header
- List of links to external resources (tecmint.com etc.)

**Proposed Fix:** Add LOG header + metadata, convert to reference format.

---

### 15. The-Warning-Message-Understand-pacnew.md (P1)

**Issues Found:**
- Missing metadata block only
- No `LOG: [LEARN]` header
- Good content on `.pacnew` handling

**Proposed Fix:** Add LOG header + metadata, wrap lines at 72 cols.

---

### 16. Updating-Archcraft-Hooks-OS-Specific.md (P1)

**Issues Found:**
- Missing metadata block only
- No `LOG: [LEARN]` header
- Session/log content (opencode session)

**Proposed Fix:** Add minimal metadata + LOG header (Debug type).

---

### 17. create-archcraft-usb.md (P1)

**Issues Found:**
- 5 lines >72 cols
- 3 headers
- 1 trailing whitespace
- Missing metadata block
- No `LOG: [LEARN]` header
- Good `dd` content

**Proposed Fix:** Add LOG header + metadata, wrap lines, fix headers.

---

### 18. Tails_Install_On_Linux.md (P1)

**Issues Found:**
- 19 lines >72 cols
- 3 headers
- 1 trailing whitespace
- Missing final newline
- Missing metadata block
- No `LOG: [LEARN]` header
- Good Tails installation content (GnuPG verification + dd)

**Proposed Fix:** Add LOG header + metadata, wrap lines, add final newline.

---

## Approval Request

Please review the above diffs. For each file, respond with:
- **APPROVE** — apply as proposed
- **MODIFY** — specify changes
- **SKIP** — don't modify this file
- **REVIEW** — need to see full corrected content first

Batch will be applied after your approval.