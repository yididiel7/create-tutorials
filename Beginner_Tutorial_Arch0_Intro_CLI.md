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