LOG: [LEARN] Reference: Arch Linux Locale Configuration and Troubleshooting

**Title:** Check Locale Installation Packages
**Date:** 2026-02-11 (20:43:04 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Check-Locale-Installation-Packages_2026-02-11_20-43-04.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Understanding .pacnew Files
When `locale.gen` is modified and updated:
```bash
$ diff /etc/locale.gen /etc/locale.gen.pacnew
```
- `169d168` — line deleted from second file
- `517a517,522` — lines added to second file

### Fix Locale Warning: "cannot change locale (en_US.UTF-8)"

#### Step 1: Edit /etc/locale.gen
```bash
$ sudo vim /etc/locale.gen
# Uncomment: en_US.UTF-8 UTF-8
# Uncomment other needed locales
```

#### Step 2: Generate Locales
```bash
$ sudo locale-gen
```

#### Step 3: Set System Locale
```bash
$ sudo vim /etc/locale.conf
# Add: LANG=en_US.UTF-8
```

#### Step 4: Apply to Current Session
```bash
$ export LANG=en_US.UTF-8
$ export LC_ALL=en_US.UTF-8
```

## The "Blueprint" (The Why/Logic)

### Locale Files Hierarchy
1. `/etc/locale.gen` — available locales (uncomment to enable)
2. `/etc/locale.conf` — system default locale
3. `~/.config/locale.conf` — user override (optional)
4. Environment variables — session override

### locale-gen vs update-locale
- `locale-gen` — Arch standard, reads `/etc/locale.gen`
- `update-locale` — Debian/Ubuntu only, not on Arch

### Common Locale Variables
| Variable | Purpose |
|----------|---------|
| `LANG` | Default locale |
| `LC_ALL` | Overrides all LC_* |
| `LC_MESSAGES` | Message language |
| `LC_TIME` | Date/time format |

## The "Deep Dive" (The Technical Root)

### diff Output Format
```
169d168       # delete line 169 from file 2
517a517,522   # append lines 517-522 after line 517 in file 2
```

### Locale Generation Internals
- `locale-gen` runs `localedef` for each uncommented line
- Creates `/usr/lib/locale/locale-archive`
- Binary format for fast runtime lookup

### Troubleshooting Checklist
1. `locale -a` — list generated locales
2. `locale` — show current settings
3. `/etc/locale.gen` — check uncommented lines
4. `/etc/locale.conf` — check LANG
5. Reboot or relogin after changes

### References
- `man locale-gen`, `man locale.conf`
- [Arch Wiki: Locale](https://wiki.archlinux.org/title/Locale)
- [GNU gettext: Locale](https://www.gnu.org/software/gettext/manual/html_node/Locale.html)