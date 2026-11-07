LOG: [LEARN] Reference: Essential System Administration Commands

**Title:** SysAdmin Linux Commands
**Date:** 2026-02-13 (06:09:04 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** SysAdmin-Linux-Commands.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### File & Timestamp Management
```bash
# touch — create files, update timestamps
$ touch file.txt                    # create or update mtime/atime
$ touch -a file.txt                 # update access time only
$ touch -m file.txt                 # update modification time only
$ touch -d "2024-01-01 12:00" file.txt  # set specific timestamp
$ touch -r reference.txt file.txt   # copy timestamp from reference

# Multiple files
$ touch file1 file2 file3
$ touch {1..10}.txt                 # brace expansion
```

### User Identity
```bash
$ whoami                            # current effective user
$ id                                # detailed user/group info
$ logname                           # login name (from utmp)
$ w                                 # who is logged in
$ who                               # logged in users
```

### Service Management (systemd)
```bash
$ systemctl start service           # start now
$ systemctl stop service            # stop now
$ systemctl restart service         # restart
$ systemctl reload service          # reload config
$ systemctl enable service          # enable at boot
$ systemctl disable service         # disable at boot
$ systemctl status service          # check status
$ systemctl list-units --type=service  # list all services
```

### Shell & Output
```bash
# echo — print text
$ echo "hello"
$ echo -n "no newline"
$ echo -e "interpret\tescapes"
$ echo $VAR                         # variable value
$ echo "$VAR"                       # preserve whitespace
$ echo > file.txt                   # write to file (truncate)
$ echo >> file.txt                  # append to file
```

### Bash Variables
```bash
$ declare -i num=42                 # integer
$ declare -r readonly_var="value"   # read-only
$ declare -a arr=(a b c)            # array
$ declare -A assoc=(["k"]="v")      # associative array
$ declare -p var                    # show attributes
```

### File Transfer (SFTP)
```bash
$ sftp user@host                    # connect
sftp> put local.txt remote.txt      # upload
sftp> get remote.txt local.txt      # download
sftp> ls                            # remote list
sftp> lls                           # local list
sftp> chmod 644 remote.txt          # remote chmod
sftp> !command                      # local shell command
```

### Network Scanning (nmap)
```bash
$ nmap 192.168.1.0/24               # ping scan
$ nmap -p 80,443 target             # specific ports
$ nmap -sS target                   # SYN scan
$ nmap -O target                    # OS detection
$ nmap -sV target                   # service versions
$ nmap -A target                    # aggressive (OS + version + scripts)
$ nmap -iL targets.txt              # scan from file
```

### Kernel Version
```bash
$ uname -r                          # kernel release
$ uname -a                          # all info
$ hostnamectl                       # systemd hostnamectl
$ cat /proc/version                 # procfs
```

### Command Location
```bash
$ which command                     # first in PATH
$ which -a command                  # all in PATH
$ type command                      # shell builtin/alias/function
$ command -v command                # POSIX standard
```

### Kernel Parameters (sysctl)
```bash
$ sysctl -a                         # all parameters
$ sysctl kernel.param               # show one
$ sysctl -w kernel.param=value      # runtime change
$ sysctl -p /etc/sysctl.d/99-custom.conf  # load config
$ sysctl --system                   # load all
```

## The "Blueprint" (The Why/Logic)

### Command Categories for Sysadmins
| Category | Core Commands |
|----------|---------------|
| Files | touch, cp, mv, rsync, find |
| Users | whoami, id, useradd, usermod |
| Services | systemctl, journalctl |
| Network | ss, ip, nmap, ping |
| Kernel | uname, sysctl, dmesg |
| Shell | bash, declare, echo |

### Arch Linux Specifics
- `systemctl` only (no `service` command)
- `pacman` for packages (not apt/yum/dnf)
- `journalctl` for logs (not /var/log/messages)

## The "Deep Dive" (The Technical Root)

### systemd Unit Types
| Type | Suffix | Purpose |
|------|--------|---------|
| Service | `.service` | Daemons |
| Socket | `.socket` | Socket activation |
| Timer | `.timer` | Scheduled tasks |
| Mount | `.mount` | Filesystem mounts |

### sysctl Persistence
```
/etc/sysctl.d/
  99-sysadmin.conf    # custom settings (loaded last)
  50-default.conf     # distribution defaults
```
Run `sysctl --system` to apply all.

### References
- `man systemctl`, `man sysctl`, `man nmap`
- [Arch Wiki: systemd](https://wiki.archlinux.org/title/systemd)
- [Arch Wiki: Network configuration](https://wiki.archlinux.org/title/Network_configuration)