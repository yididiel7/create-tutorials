# Plan: Organize Tutorial Directory into Logical Groups

**Date:** 2026-11-04
**Goal:** Reorganize 164 markdown files in `/home/srhills/labs/experiments/create-tutorials` into a logical, navigable directory structure grouped by topic/domain.

---

## Current Context / Assumptions

- **Root directory:** `/home/srhills/labs/experiments/create-tutorials`
- **Total files:** 164 `.md` files (plus some `.aux`, `.log`, `.tex`, `.lua`, `.bak`, `.sh` files)
- **Existing subdirectories:** `Niri-Guides/` (7 files), `Nm-Arch-Guide/` (2 files), `Fabric-Clipb-Integ-Comp-Solution/` (1 file)
- **Naming convention per AGENTS.md:** `Title-Case-With-Dashes.md` format, 72-column line breaks
- **Required metadata block:** Title, Date, Author, lfnc, Copyright, License (per AGENTS.md)
- **No build system** — pure documentation project
- **User preference:** Concise, direct, action-oriented; verify before acting

---

## Architecture / Proposed Approach

Create a **two-level directory hierarchy** by topic domain. Each top-level directory represents a major category (e.g., `Arch-Linux/`, `Terminal-Shell/`, `Editors-IDEs/`). Files move into the most specific matching directory. Preserve existing subdirectories (`Niri-Guides/`, `Nm-Arch-Guide/`) as they already follow this pattern. Create an `INDEX.md` at root for navigation.

**Categories identified (12 groups):**

| Category | Directory Name | File Count (est.) |
|----------|----------------|-------------------|
| Arch Linux System Admin | `Arch-Linux/` | ~25 |
| Window Managers / Compositors | `Window-Managers/` | ~10 |
| Terminal & Shell | `Terminal-Shell/` | ~20 |
| Editors & IDEs | `Editors-IDEs/` | ~15 |
| AI / ML Tools | `AI-ML-Tools/` | ~12 |
| Network & NetworkManager | `Network/` | ~8 |
| File Managers | `File-Managers/` | ~4 |
| System Utilities (disk, fsck, etc.) | `System-Utilities/` | ~10 |
| Development Tools (Git, UV, Python) | `Development-Tools/` | ~12 |
| Desktop Environment / UI | `Desktop-UI/` | ~8 |
| Security & Firewall | `Security/` | ~5 |
| Virtualization & Installation Media | `Virtualization/` | ~8 |
| Meta / Session / Reference | `Meta-Reference/` | ~15 |

**Total categorized:** ~162 files (some files may fit multiple categories — assign to best fit)

---

## Step-by-Step Tasks

Each task is a bite-sized move operation (2–5 min). Tasks are ordered by category for logical flow. All moves use `mv` with verification.

### Task 1: Create Directory Structure
```bash
cd /home/srhills/labs/experiments/create-tutorials
mkdir -p Arch-Linux Window-Managers Terminal-Shell Editors-IDEs AI-ML-Tools Network File-Managers System-Utilities Development-Tools Desktop-UI Security Virtualization Meta-Reference
```

**Verification:**
```bash
ls -d */
# Should show 12 new directories + 3 existing
```

---

### Task 2: Move Arch Linux System Administration Files
**Target:** `Arch-Linux/`
```bash
mv "Arch_Linux_command-line_commands.md" Arch-Linux/
mv "archiso_build_install.md" Arch-Linux/
mv "Beginner_Tutorial_Arch0_Intro_CLI.md" Arch-Linux/
mv "build-llama.cpp-on-Arch-Linux.md" Arch-Linux/
mv "Check-Locale-Installation-Packages_2026-02-11_20-43-04.md" Arch-Linux/
mv "configuring-a-new-kvm-on-arch-linux-using-qemu-cli.md" Arch-Linux/
mv "Create-a-New-VENV-Installing-UV-on-Archlinux.md" Arch-Linux/
mv "Customizing-Your-Linux-System-with-User-Management.md" Arch-Linux/
mv "GPF_Hard_Drive_In_Arch_Linux.md" Arch-Linux/
mv "how-do-i-properly-install-kvm-on-arch-linux.md" Arch-Linux/
mv "Instruct-Command-for-Package-Management.md" Arch-Linux/
mv "Install_Setup-and-enable-the_Auditd_service.md" Arch-Linux/
mv "Powerful-Command-line-Installation-Commands.md" Arch-Linux/
mv "SysAdmin-Linux-Commands.md" Arch-Linux/
mv "The-Warning-Message-Understand-pacnew.md" Arch-Linux/
mv "Updating-Archcraft-Hooks-OS-Specific.md" Arch-Linux/
mv "create-archcraft-usb.md" Arch-Linux/
mv "Tails_Install_On_Linux.md" Arch-Linux/
```

**Verification:**
```bash
ls Arch-Linux/ | wc -l
# Expect ~18 files
```

---

### Task 3: Move Window Manager / Compositor Files
**Target:** `Window-Managers/`
```bash
# Move existing Niri-Guides into Window-Managers as subdirectory
mv Niri-Guides Window-Managers/
# Move loose Niri file
mv "Niri_Main_Default_Hotkeys.md" Window-Managers/Niri-Guides/
```

**Verification:**
```bash
ls Window-Managers/Niri-Guides/ | wc -l
# Expect 8 files
```

---

### Task 4: Move Terminal & Shell Files
**Target:** `Terminal-Shell/`
```bash
mv "alias-fix-keyserver-aliases.md" Terminal-Shell/
mv "bindkey-re-magic-space.md" Terminal-Shell/
mv "cannot-update-oh-my-zsh.md" Terminal-Shell/
mv "Edit-Command-Buffer-Fix.md" Terminal-Shell/
mv "Fix-No-GTK-environment-variables-in-shell-configs-session-ses_3b3e.md" Terminal-Shell/
mv "Kitty-Color-Schemes-How-to-Change.md" Terminal-Shell/
mv "Kitty-Neovim-Performance-Optimization-Plan.md" Terminal-Shell/
mv "readline-cheatsheet.md" Terminal-Shell/
mv "starship-install-config.md" Terminal-Shell/
mv "Tmux-display-popup-custom-configuration.md" Terminal-Shell/
mv "Tmuxifier-Quick-Start-fix.md" Terminal-Shell/
mv "tmux-status-bar-styling-with-Catppuccin-arrows.md" Terminal-Shell/
mv "warp-terminal-install-errors-corrected.md" Terminal-Shell/
mv "warp_key.md" Terminal-Shell/
mv "zle _expand_history_error_fix.md" Terminal-Shell/
mv "zsh-fix-bindkey-space.md" Terminal-Shell/
mv "ZSH-Hacks-Dreams-of-Code.md" Terminal-Shell/
mv "zshrc_Personal-FebUpd-1126_1.md" Terminal-Shell/
mv "zsh_To_fix_a_corrupt_zsh_history_file.md" Terminal-Shell/
```

**Verification:**
```bash
ls Terminal-Shell/ | wc -l
# Expect ~19 files
```

---

### Task 5: Move Editors & IDEs Files
**Target:** `Editors-IDEs/`
```bash
mv "Analyze-the-codebase-for-torch-and-nvim.md" Editors-IDEs/
mv "Base16-Colorschemes-for-Geany.md" Editors-IDEs/
mv "Creating-Custom-Fabric-Patterns-✂️.md" Editors-IDEs/
mv "editor-terminal-functions.md" Editors-IDEs/
mv "Editing_Text_in_Vim_by_Selecting_and_Replacing_2026-01-24_17-58-47.md" Editors-IDEs/
mv "fisa-vim-configuration-file.md" Editors-IDEs/
mv "fisadevSetupforvimrcPyton.md" Editors-IDEs/
mv "GEANY_PROJECT_SETUP.md" Editors-IDEs/
mv "GEANY_SETUP_GUIDE.md" Editors-IDEs/
mv "Geany-startup-logs-and-error-debugging.md" Editors-IDEs/
mv "How_to_Copy_in_Vim.md" Editors-IDEs/
mv "How_to_paste_in_vim.md" Editors-IDEs/
mv "neovim-deleting-the-existing-dot-git-folder.md" Editors-IDEs/
mv "Neovim-Help-System-Commands-and-Keys.md" Editors-IDEs/
mv "Neovim-keybindings-not-working-cheatsheet-check.md" Editors-IDEs/
mv "neovim-leader-key-maps.md" Editors-IDEs/
mv "nvchad_to_change_the_statusline_style_in_NVChad.md" Editors-IDEs/
mv "NvimTreeResize.md" Editors-IDEs/
mv "nvim_Updated_pacman_pkg_installed.md" Editors-IDEs/
mv "null-ls-nvim-fixed.md" Editors-IDEs/
mv "setting_marks_in_vim.md" Editors-IDEs/
mv "vim_reference_editing_commands.md" Editors-IDEs/
mv "vimhelp-in-avert-split.md" Editors-IDEs/
mv "vscode" -> (no vscode files found, skip)
mv "Which_key_conflicts.md" Editors-IDEs/
```

**Verification:**
```bash
ls Editors-IDEs/ | wc -l
# Expect ~24 files
```

---

### Task 6: Move AI / ML Tools Files
**Target:** `AI-ML-Tools/`
```bash
mv "Advanced-Research-Assistant.md" AI-ML-Tools/
mv "Common-ollama-interactive-commands.md" AI-ML-Tools/
mv "Fabric-AI-tab-autocompletion-error.md" AI-ML-Tools/
mv "fabric-ai-tab-autocompletion-issue-session-ses_3b77.md" AI-ML-Tools/
mv "Fabric-Clipb-Integ-Comp-Solution" AI-ML-Tools/  # move entire dir
mv "Fabric-Fixed-Error-Analysis-And-Shell-Completion-Review.md" AI-ML-Tools/
mv "FABRIC-SOLUTION.md" AI-ML-Tools/
mv "fabric-usage-guide.md" AI-ML-Tools/
mv "FHD_Prompt_BestResults_Deep-v3_1_671b_cloud.md" AI-ML-Tools/
mv "Learn-to-use-Ollama-in-the-terminal.md" AI-ML-Tools/
mv "Ollama-CLI-tricks.md" AI-ML-Tools/
mv "Opencode-AI-Capabilities.md" AI-ML-Tools/
mv "Opencode-run--attach-connection-to-running-server.md" AI-ML-Tools/
mv "PromptMaxer.md" AI-ML-Tools/
mv "Prompt-Rewrite-Reforge-Markdown-Files.md" AI-ML-Tools/
mv "The-Best-ChatGPT-Prompts-Ever-Written.md" AI-ML-Tools/
```

**Verification:**
```bash
ls AI-ML-Tools/ | wc -l
# Expect ~16 files + 1 subdir
```

---

### Task 7: Move Network & NetworkManager Files
**Target:** `Network/`
```bash
# Move existing Nm-Arch-Guide into Network as subdirectory
mv Nm-Arch-Guide Network/
# Move loose Nmcli file
mv "Nmcli-a-Powerful-Command-line-tool.md" Network/Nm-Arch-Guide/
# Other network files
mv "twingate-fast-cuscus-connector_1.md" Network/
mv "twingate-fast-cuscus-connector.md" Network/
mv "ufw_setup_firewall_in_Linux.md" Network/
```

**Verification:**
```bash
ls Network/Nm-Arch-Guide/ | wc -l
# Expect 3 files
ls Network/ | wc -l
# Expect 4 files + 1 subdir
```

---

### Task 8: Move File Manager Files
**Target:** `File-Managers/`
```bash
mv "Yazi-Quick-Start-Key-Navigation.md" File-Managers/
mv "Yazi_other_keybindings_can_follow_mgr_prepend_keymap.md" File-Managers/
```

**Verification:**
```bash
ls File-Managers/ | wc -l
# Expect 2 files
```

---

### Task 9: Move System Utilities Files
**Target:** `System-Utilities/`
```bash
mv "check-for-memory-fragmentation-on-Arch-Linux.md" System-Utilities/
mv "content_raw_cfdisk.md" System-Utilities/
mv "DIY_Partition_formatting_with_cfdisk.md" System-Utilities/
mv "DIY_Sample3_tutorial.md" System-Utilities/
mv "fdisk_cfdisk.md" System-Utilities/
mv "Partition_FHD_Util_Cfdisk_Arch.md" System-Utilities/
mv "Understanding_the_Command_sudo_cfdisk_l.md" System-Utilities/
mv "using-the-fsck-command.md" System-Utilities/
mv "Gdk-Critical-fix-transient_for-assertion-failed.md" System-Utilities/
mv "Meld-GTK-NoneType-error-with-grub-pacnew-files.md" System-Utilities/
```

**Verification:**
```bash
ls System-Utilities/ | wc -l
# Expect ~10 files
```

---

### Task 10: Move Development Tools Files
**Target:** `Development-Tools/`
```bash
mv "add-folders-to-a-GitHub-repository-using-the-command-line.md" Development-Tools/
mv "GitButler-Cli-Install.md" Development-Tools/
mv "Git-clone-failure-destination-exists-for-inir-repo.md-session-ses_3c7a.md" Development-Tools/
mv "Git-How-to-Make-a-Folder-in-GitHub.md" Development-Tools/
mv "Grep_Search_Patterns_Files.md" Development-Tools/
mv "lookup-flag-meaning-of-each-package-manager.md" Development-Tools/
mv "Pythoh-guide-for-unit-module-testing-00.md" Development-Tools/
mv "Python-Test-Driven-Development.md" Development-Tools/
mv "To_search_for_patterns_in_files_using_grep.md" Development-Tools/
mv "UV_how_to_Install_uv.md" Development-Tools/
mv "uv-python-manager.md" Development-Tools/
mv "uv-python-package-manager.md" Development-Tools/
mv "create_prompt_tutorial.md" Development-Tools/
mv "create_prompt_tutorial_1.md" Development-Tools/
mv "refactor_markdown_prompt.md" Development-Tools/
mv "format_markdown_txt.md" Development-Tools/
```

**Verification:**
```bash
ls Development-Tools/ | wc -l
# Expect ~16 files
```

---

### Task 11: Move Desktop UI Files
**Target:** `Desktop-UI/`
```bash
mv "firefox-keyboard-shortcuts.md" Desktop-UI/
mv "Fix-Rofi-config-color-mismatch.md" Desktop-UI/
mv "how-to-install-sweet-dark-v40.tar.xz-theme.md" Desktop-UI/
mv "logo-colors-hex.md" Desktop-UI/
mv "Polybar-Texts-Settings.md" Desktop-UI/
mv "To-install-ter-powerline-v18n-vconsolefont.md" Desktop-UI/
mv "xfcepolicykit-agent-GDBus-Error-org-freedesktop.md" Desktop-UI/
```

**Verification:**
```bash
ls Desktop-UI/ | wc -l
# Expect ~7 files
```

---

### Task 12: Move Security & Firewall Files
**Target:** `Security/`
```bash
mv "alias-fix-keyserver-aliases.md" Security/  # already moved in Task 4, skip
# Actually keyserver aliases is more terminal/shell - keep in Terminal-Shell
# Security-specific files:
mv "ufw_setup_firewall_in_Linux.md" Security/  # already moved in Task 7
# Let's check for dedicated security files...
# Install_Setup-and-enable-the_Auditd_service.md -> already in Arch-Linux
# No other obvious security files. Keep Security/ minimal or merge.
```

**Note:** Most security-related files are already categorized. May keep `Security/` for future or remove if empty.

---

### Task 13: Move Virtualization & Installation Media Files
**Target:** `Virtualization/`
```bash
mv "configuring-a-new-kvm-on-arch-linux-using-qemu-cli.md" Virtualization/  # already in Arch-Linux
mv "how-do-i-properly-install-kvm-on-arch-linux.md" Virtualization/  # already in Arch-Linux
mv "archiso_build_install.md" Virtualization/  # already in Arch-Linux
mv "create-archcraft-usb.md" Virtualization/  # already in Arch-Linux
mv "Tails_Install_On_Linux.md" Virtualization/  # already in Arch-Linux
# These are already in Arch-Linux. Create symlinks or leave as-is.
# Decision: Leave in Arch-Linux, create Virtualization/ with README linking to them.
```

**Revised approach:** Create `Virtualization/` with a `README.md` linking to relevant Arch-Linux files, rather than duplicating.

---

### Task 14: Move Meta / Session / Reference Files
**Target:** `Meta-Reference/`
```bash
mv "AGENTS.md" Meta-Reference/
mv "Document-heading-auto-populate-for-AGENTS.md" Meta-Reference/
mv "RepoTask-01-CreateTutorials-Reformatted-100-Markdown-Files.md" Meta-Reference/
mv "session-ses_3b75.md" Meta-Reference/
mv "session-ses_3b9d.md" Meta-Reference/
mv "session-ses_3bdc.md" Meta-Reference/
mv "session-ses_3c7a.md" Meta-Reference/
mv "session-ses_3c87.md" Meta-Reference/
mv "session-ses_47ae.md" Meta-Reference/
mv "QS-Inst-Analysis-SUMMARY-session-ses_3c11.md" Meta-Reference/
mv "chat-📄-Refactoring-Markdown-Instructions.md" Meta-Reference/
mv "chat-Understanding-the-sort-Command.md" Meta-Reference/
mv "copilot-session-e1ebe014-169b-4ade-9855-454c2df7019f.md" Meta-Reference/
mv "history-bk1-backup.md" Meta-Reference/
mv "Memory-Optimization-Tasks-Completed.md" Meta-Reference/
mv "test-header.sh" Meta-Reference/
mv "to-add-files.md.bak" Meta-Reference/
mv "NvChad-mappings.lua" Meta-Reference/
mv "DUCKDUCKGO_SEARCH-ERROR.md" Meta-Reference/  # check exact name
mv "duck.ai_2025-11-20_07-20-20.md" Meta-Reference/
mv "conference_call_on_hfd_aid.md" Meta-Reference/
mv "SHA_Leadership_Confcallconference_call_on_hfd_aid.md" Meta-Reference/
mv "SlashDot_Account.md" Meta-Reference/
mv "PyPI_Account_Recovery_Codes.md" Meta-Reference/
mv "YH-PP00-09FEB26.md" Meta-Reference/
mv "TELOS_background_information.md" Meta-Reference/
mv "MY_TELOS_FILE.md" Meta-Reference/
mv "numerological-name-Yididiel-meaning.md" Meta-Reference/
mv "Psychological-Profile-Sr-Yididiel-Hills.md" Meta-Reference/
mv "Confidential-Executive-Psychological-Overview.md" Meta-Reference/
mv "Human_Resources_prompts.md" Meta-Reference/
mv "politics-and-quotes.md" Meta-Reference/
mv "Atuin-Search-Analysis-Complete.md" Meta-Reference/
mv "PC-Performance-Analysis-Complete.md" Meta-Reference/
mv "Installed-Fresh-Editor-v0.1.99.md" Meta-Reference/
mv "myenv-hf_Config.md" Meta-Reference/
mv "Huggingface-project-directory.md" Meta-Reference/
mv "Paperless_Digities_Your_Life.md" Meta-Reference/
mv "generate-random-man-pages.md" Meta-Reference/
```

**Verification:**
```bash
ls Meta-Reference/ | wc -l
# Expect ~35 files
```

---

### Task 15: Create Root INDEX.md Navigation File
Create `/home/srhills/labs/experiments/create-tutorials/INDEX.md` with a table of contents linking to each category directory.

**Content structure:**
```markdown
# Tutorial Index

## Categories
- [Arch Linux](Arch-Linux/) — System administration, installation, package management
- [Window Managers](Window-Managers/) — Niri, compositors, Wayland
- [Terminal & Shell](Terminal-Shell/) — Zsh, Tmux, Kitty, Warp, Starship
- [Editors & IDEs](Editors-IDEs/) — Neovim, Geany, NVChad, Vim
- [AI / ML Tools](AI-ML-Tools/) — Ollama, Fabric, OpenCode, PromptMaxer
- [Network](Network/) — NetworkManager, nmcli, Twingate, UFW
- [File Managers](File-Managers/) — Yazi
- [System Utilities](System-Utilities/) — Disk partitioning, fsck, cfdisk
- [Development Tools](Development-Tools/) — Git, UV, Python, Grep, Prompts
- [Desktop UI](Desktop-UI/) — Firefox, Rofi, Polybar, Themes
- [Meta & Reference](Meta-Reference/) — AGENTS.md, sessions, configs, personal notes
```

---

### Task 16: Verify All Files Accounted For
```bash
cd /home/srhills/labs/experiments/create-tutorials
find . -name "*.md" -type f | wc -l
# Should still be 164 (no files lost)

# Check each directory
for d in Arch-Linux Window-Managers Terminal-Shell Editors-IDEs AI-ML-Tools Network File-Managers System-Utilities Development-Tools Desktop-UI Security Virtualization Meta-Reference; do
  echo "$d: $(find "$d" -name "*.md" -type f | wc -l)"
done
```

---

### Task 17: Validate Markdown Syntax (Optional)
```bash
# If markdownlint available
markdownlint */*.md
# Or check for obvious issues
```

---

## Tests / Validation

| Check | Command | Expected |
|-------|---------|----------|
| Total file count preserved | `find . -name "*.md" -type f | wc -l` | 164 |
| No files in root (except INDEX.md, AGENTS.md) | `ls *.md` | ≤2 files |
| All 12 category dirs exist | `ls -d */ | grep -c` | ≥12 |
| INDEX.md created and readable | `head -20 INDEX.md` | Shows TOC |
| Existing subdirs preserved | `ls Window-Managers/Niri-Guides/` | 8 files |

---

## Risks, Tradeoffs, and Open Questions

| Risk / Question | Mitigation / Decision |
|----------------|------------------------|
| **Duplicate categorization** — some files fit multiple categories (e.g., `build-llama.cpp-on-Arch-Linux.md` is both Arch-Linux and AI-ML-Tools) | Assign to **primary** category; add cross-reference in INDEX.md. Primary = where user would first look. |
| **Session/log files** — large session files (`session-ses_*.md`, `copilot-session-*.md`) clutter Meta-Reference | Keep in Meta-Reference; they're reference/debug artifacts. Consider archiving older ones later. |
| **Non-markdown files** — `.lua`, `.sh`, `.bak`, `.aux`, `.log`, `.tex` | Leave in Meta-Reference or create `Assets/` subdir. Not part of tutorial set. |
| **Filename collisions** — two files with same name in different dirs | Not observed in current inventory. If occurs, prefix with category short-name. |
| **AGENTS.md location** — currently in root, referenced by agents | Move to `Meta-Reference/AGENTS.md` AND keep symlink at root, or update agent config. **Decision:** Move to Meta-Reference, add symlink at root for backward compatibility. |
| **Date metadata updates** — AGENTS.md says "Update date metadata when substantially modifying" | Moving files ≠ modifying content. No date updates needed. |
| **Virtualization category** — sparse, overlaps heavily with Arch-Linux | Create `Virtualization/README.md` with links instead of moving files. Avoids duplication. |
| **Security category** — nearly empty after moves | Keep for future; or merge into `System-Utilities/`. **Decision:** Keep empty dir with README. |

---

## Execution Notes for Implementer

1. **Run tasks sequentially** — each `mv` depends on directories existing from Task 1.
2. **Verify after each task** — run the verification command before proceeding.
3. **If a file is missing** — check if already moved in a prior task (e.g., `ufw_setup_firewall_in_Linux.md` appears in both Task 7 and Task 12).
4. **Use exact filenames** — the list above uses exact names from `ls` output (spaces, underscores, special chars preserved).
5. **Create INDEX.md last** — after all moves complete so links are accurate.
6. **Commit after verification** — if using git, commit after Task 16 passes.

---

## Plan Saved To
`.hermes/plans/2026-11-04_134452-organize-tutorial-directory.md`