LOG: [LEARN] Guide: Fix Kitty + Neovim Performance Issues

**Title:** Kitty Neovim Performance Optimization Plan
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Kitty-Neovim-Performance-Optimization-Plan.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Immediate Wins (5-10 min)

#### 1. Kitty Config Optimizations
```bash
# ~/.config/kitty/kitty.conf
background_opacity 1.0          # Disable transparency (major perf win)
repaint_delay 8                 # Lower = smoother (default 10)
input_delay 2                   # More responsive (default 3)
sync_to_monitor yes             # Prevent tearing
scrollback_lines 2500           # Reduce from 5000
cursor_blink_interval 0         # Disable blinking
disable_ligatures always        # Better perf
enable_audio_bell no
visual_bell_duration 0.0
```

#### 2. Neovim Cache Cleanup
```bash
# Check space usage
$ du -sh ~/.local/share/nvim/* | sort -hr

# Clean swap/shada
$ rm -rf ~/.local/state/nvim/swap/*
$ rm -rf ~/.local/state/nvim/shada/*

# Clean base46 compiled themes (NvChad)
$ rm -rf ~/.local/share/nvim/nvchad/base46/*

# Recompile clean
$ nvim --headless -c 'lua require("base46").load_all_highlights()' -c 'qa'
```
Expected: 754MB → ~100-200MB

#### 3. Plugin Lazy-Loading
```lua
-- ~/.config/nvim/lua/custom/plugins.lua
{ 'Exafunction/codeium.vim', event = 'InsertEnter' },
{ 'mfussenegger/nvim-dap', cmd = { 'DapContinue', 'DapToggleBreakpoint' } },
{ 'rcarriga/nvim-dap-ui', dependencies = { 'mfussenegger/nvim-dap' }, cmd = 'DapContinue' },
{ 'simrat39/symbols-outline.nvim', cmd = { 'SymbolsOutline', 'SymbolsOutlineOpen' } },
{ 'folke/noice.nvim', event = 'VeryLazy', cond = function() return vim.fn.has('nvim-0.9') == 1 end },
```

### Deep Optimization (20-30 min)

#### 4. Plugin Audit
```bash
# Profile startup
$ nvim --startuptime /tmp/startup.log -c 'qa!'
$ cat /tmp/startup.log | sort -k2 -nr | head -20

# List plugins with load times
$ nvim --headless -c 'lua require("lazy").stats()' -c 'qa' 2>&1 | head -50
```

#### 5. Remove Unused Plugins
- DAP plugins if not debugging
- Go-specific plugins if not using Go
- Replace `noice.nvim` with `j-hui/fidget.nvim` (lighter)
- Use built-in LSP formatting instead of `none-ls`

## The "Blueprint" (The Why/Logic)

### Performance Priority
| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 🔴 P0 | Disable kitty transparency | HIGH | 1 min |
| 🔴 P0 | Clean 754MB nvim cache | HIGH | 2 min |
| 🟡 P1 | Lazy-load codeium.vim | HIGH | 2 min |
| 🟡 P1 | Lazy-load DAP plugins | HIGH | 5 min |
| 🟡 P1 | Kitty repaint_delay | MED | 1 min |
| 🟢 P2 | Remove unused plugins | MED | 10 min |
| 🔵 P3 | Replace noice.nvim | LOW | 15 min |

### Root Causes
| Component | Issue | Fix |
|-----------|-------|-----|
| Kitty | `background_opacity 0.8` | GPU compositing overhead |
| Nvim | 754MB base46 cache | Stale compiled themes |
| Plugins | `event = 'BufEnter'` on heavy plugins | Loads on every buffer |
| Kitty | Ligatures enabled | Font shaping cost |

## The "Deep Dive" (The Technical Root)

### Kitty Rendering Pipeline
```
Input → Parser → Grid → Renderer (GPU) → Display
              ↑
         Transparency adds blend pass
         Ligatures add font shaping
```

### Neovim Startup Phases
```
1. Init vim runtime
2. Load lazy.nvim
3. Load plugin specs (parallel)
4. Run plugin config()
5. Source after/ftplugin
6. Draw UI
```

### Profiling Commands
```bash
# Kitty bench
$ kitty +bench

# Nvim detailed startup
$ nvim --startuptime /tmp/startup.log -c 'qa!'
$ cat /tmp/startup.log | head -30

# Continuous monitoring
nvim() {
    local start=$EPOCHREALTIME
    command nvim "$@"
    local elapsed=$((EPOCHREALTIME - start))
    (( elapsed > 0.5 )) && echo "⚠️ Nvim took ${elapsed}s"
}
```

### Expected Results
- Kitty: Smoother scroll, less GPU/CPU
- Nvim: Startup < 150ms (from 500ms+)
- Disk: 600MB+ freed

### References
- [Kitty Performance](https://sw.kovidgoyal.net/kitty/faq/#performance)
- [Lazy.nvim Profiling](https://github.com/folke/lazy.nvim#profiling)
- [NvChad Base46](https://github.com/NvChad/base46)