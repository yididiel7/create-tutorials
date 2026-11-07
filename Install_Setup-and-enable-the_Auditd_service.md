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