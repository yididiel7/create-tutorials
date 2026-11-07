LOG: [LEARN] Reference: Arch Linux Command-Line Commands

**Title:** Arch Linux Command-Line Commands
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Arch_Linux_command-line_commands.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Basic Commands
```bash
$ ls              # list files and directories
$ cd              # change directory
$ pwd             # print working directory
$ mkdir           # make a new directory
$ rm              # remove a file or directory
$ touch           # create a new empty file
$ cp              # copy a file
$ mv              # move or rename a file
$ echo            # print text to the console
$ cat             # read text from a file
```

### File Management
```bash
$ ls -l                   # detailed listing
$ find .                  # search files recursively
$ grep pattern            # search patterns in files
$ awk 'pattern' file      # process text with awk
$ sed 'pattern' file      # stream edit with sed
$ rsync -avz src dest     # synchronize files
```

### User Management
```bash
$ useradd username        # create user
$ userdel username        # delete user
$ groups username         # list user groups
$ gpasswd groupname       # manage group membership
$ su                      # switch user
$ sudo                    # run as superuser
```

### System Administration
```bash
$ systemctl start service    # start service
$ systemctl stop service     # stop service
$ systemctl enable service   # enable at boot
$ systemctl disable service  # disable at boot
$ journalctl                 # view system logs
$ logrotate log_file         # rotate logs
$ ufw status                 # firewall status
```

### Networking
```bash
$ ping hostname           # test connectivity
$ nslookup hostname       # DNS lookup
$ dig hostname            # detailed DNS query
$ ip addr show            # show network addresses
$ ip route                # show routing table
```

### System Monitoring
```bash
$ top                     # process list
$ htop                    # interactive process viewer
$ vmstat                  # virtual memory stats
$ sar                     # system activity report
```

### Security
```bash
$ chown user:group path   # change ownership
$ chmod +x script         # make executable
$ ss -lpni                # socket/process info
$ kill pid                # kill process
```

### Miscellaneous
```bash
$ date                    # current date/time
$ hostname                # system hostname
$ uptime                  # system uptime
$ free -h                 # memory usage
$ lscpu                   # CPU info
```

## The "Blueprint" (The Why/Logic)

### Command Categories
Commands are grouped by functional area for quick reference. Use `man <command>` for detailed documentation.

### Arch-Specific Notes
- Package management via `pacman` (not apt/dnf)
- Service management via `systemctl` (systemd only)
- Configuration in `/etc/` following Arch conventions

## The "Deep Dive" (The Technical Root)

### uname -a Breakdown
```bash
$ uname -a
Linux arch-vm 5.15.21-arch1-1 #1 SMP PREEMPT Sat, 12 Feb 2022 13:38:47 +0000 x86_64 x86_64 x86_64 GNU/Linux
```
- `Linux` — kernel name
- `arch-vm` — hostname
- `5.15.21-arch1-1` — kernel version
- `#1 SMP PREEMPT ...` — build info
- `x86_64 x86_64 x86_64` — machine/processor/hardware platform
- `GNU/Linux` — OS

### References
- `man <command>` for any command
- [Arch Wiki: General recommendations](https://wiki.archlinux.org/title/General_recommendations)
- [Arch Wiki: System maintenance](https://wiki.archlinux.org/title/System_maintenance)