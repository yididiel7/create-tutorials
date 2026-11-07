# Review Batch: AI-ML-Tools

**Generated:** 2026-11-04
**Files:** 17 (16 files + 1 subdirectory file)
**Standard:** 4-section format with `LOG: [LEARN]` header + Recipe/Blueprint/Deep Dive + Metadata

---

## Summary of Changes per File

### P0 Tutorials (Full Restructure + Content Verification)

| File | Primary Issues | Restructure Needed |
|------|---------------|-------------------|
| `Learn-to-use-Ollama-in-the-terminal.md` | 17 line len, 20 headers, missing metadata, no LOG, Hostinger content scraped | ✅ Full 4-section |
| `Ollama-CLI-tricks.md` | Missing metadata, no LOG, minimal content | ✅ Full 4-section |
| `Common-ollama-interactive-commands.md` | **Has metadata**, no LOG, good content | ✅ Full 4-section |
| `Ollama-CLI-tricks.md` | Missing metadata, no LOG, good reference content | ✅ Full 4-section |
| `Advanced-Research-Assistant.md` | 6 line len, 4 headers, missing metadata, no LOG, session log content | ✅ Full 4-section |
| `PromptMaxer.md` | 49 line len, 3 headers, 61 trailing, missing metadata, no LOG, complex prompt template | ✅ Full 4-section |
| `The-Best-ChatGPT-Prompts-Ever-Written.md` | Missing metadata, no LOG, CRAFT prompt template | ✅ Full 4-section |

### P1 References (Structural Fixes + Metadata + LOG Header)

| File | Primary Issues |
|------|---------------|
| `Fabric-AI-tab-autocompletion-error.md` | 1 header, **has metadata**, no LOG, session log content |
| `fabric-ai-tab-autocompletion-issue-session-ses_3b77.md` | 48 line len, 82 headers, 216 code blocks, 114 inline, 117 trailing, missing metadata, no LOG, massive session log |
| `Fabric-Fixed-Error-Analysis-And-Shell-Completion-Review.md` | 19 line len, 6 headers, 24 trailing, missing 1 meta, no LOG, session log with good content |
| `FABRIC-SOLUTION.md` | 3 line len, 19 headers, 4 code blocks, 2 inline, 2 trailing, missing metadata, no LOG, good tutorial |
| `fabric-usage-guide.md` | 1 line len, 51 headers, 17 code blocks, 9 inline, missing metadata, no LOG, comprehensive guide |
| `FHD_Prompt_BestResults_Deep-v3_1_671b_cloud.md` | 14 headers, 19 code blocks, 10 inline, **has metadata**, no LOG, prompt template |
| `Opencode-AI-Capabilities.md` | 1 header, **has metadata**, no LOG, session log |
| `Opencode-run--attach-connection-to-running-server.md` | 7 line len, 9 headers, 4 trailing, missing metadata, no LOG, short note |
| `Prompt-Rewrite-Reforge-Markdown-Files.md` | 1 header, 1 trailing, missing metadata, no LOG, short note |
| `Fabric-Clipb-Integ-Comp-Solution/Fabric-Clipboard-Integration-Complete-Solution.md` | 7 headers, **has metadata**, no LOG, good tutorial |

---

## Detailed Diffs

### 1. Learn-to-use-Ollama-in-the-terminal.md (P0)

**Issues:** Hostinger scraped content, 17 lines >72 chars, 20 headers (mixed case), missing metadata, no LOG header, duplicated code blocks

**Content Corrections:**
- Remove "Plain text / Copy to clipboard / Open code in new window / EnlighterJS 3 Syntax Highlighter" artifacts
- Fix `ollama --version` repeated 3 times
- Fix `ollama pull llama3.2` repeated 3 times
- Fix `ollama run llama3.2` repeated 3 times
- Fix `/bye` repeated 3 times
- Remove Hostinger images/links
- Fix Modelfile template duplicated 3 times
- Remove "Copy to clipboard / Open code in new window" repeated throughout
- Add proper `num_ctx` parameter info (model-specific)
- Fix `ollama create` vs `ollama pull` confusion

**Proposed Structure:**
```
LOG: [LEARN] Guide: Run Ollama Models in Terminal

**Title:** Learn to Use Ollama in the Terminal
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Learn-to-use-Ollama-in-the-terminal.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)
### Prerequisites
- Ollama installed (`curl -fsSL https://ollama.com/install.sh | sh`)
- Terminal with bash/zsh

### Basic Commands
```bash
$ ollama --version
$ ollama serve                    # Start server
$ ollama pull llama3.2            # Pull model
$ ollama list                     # List models
$ ollama run llama3.2 "prompt"    # Run with prompt
$ ollama run llama3.2             # Interactive
/bye                              # Exit interactive
```

### Model Management
```bash
$ ollama show llama3.2            # Model details
$ ollama ps                       # Running models
$ ollama stop llama3.2            # Stop model
$ ollama rm llama3.2              # Remove model
$ ollama cp llama3.2 my-model     # Copy model
```

### File I/O
```bash
$ ollama run llama3.2 "Summarize" < input.txt
$ ollama run llama3.2 "Prompt" > output.txt
$ cat input.txt | ollama run llama3.2 "Summarize"
```

### Custom Models (Modelfile)
```bash
# Modelfile
FROM llama3.2
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
SYSTEM "You are a cybersecurity expert."
TEMPLATE "{{ if .System }}System: {{ .System }}{{ end }}User: {{ .Prompt }}Assistant: "

$ ollama create my-model -f Modelfile
$ ollama run my-model
```

### Automation
```bash
#!/bin/bash
ollama run llama3.2 "AI trends" > ai-output.txt
```
```bash
# Cron: 0 0 * * 0 /path/script.sh
```

## The "Blueprint" (The Why/Logic)
### Why Ollama CLI?
- Local execution, no API keys
- Scriptable for automation
- File I/O for large documents
- Custom models via Modelfile

### Architecture
- `ollama serve` — REST API server (localhost:11434)
- Models stored in `~/.ollama/models/`
- Modelfile = Dockerfile-like blueprint

### Parameter Guide
| Param | Range | Effect |
|-------|-------|--------|
| `temperature` | 0.0–2.0 | Creativity (0=deterministic) |
| `num_ctx` | 512–128k | Context window (model max) |
| `top_p` | 0.0–1.0 | Nucleus sampling |
| `num_predict` | -1 to N | Max output tokens |

## The "Deep Dive" (The Technical Root)
### Modelfile Internals
- `FROM` — base model or GGUF path
- `PARAMETER` — runtime params
- `SYSTEM` — system prompt
- `TEMPLATE` — chat template (Go template)
- `ADAPTER` — LoRA path

### API Endpoints
```
POST /api/generate   — single completion
POST /api/chat       — conversation
POST /api/embeddings — embeddings
GET  /api/tags       — list models
```

### OpenAI Compatibility
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```

### GPU Acceleration
- NVIDIA: CUDA 5.0+, `nvidia-smi`
- AMD: ROCm, RX 6000+
- Apple: Metal (auto)
- Env: `CUDA_VISIBLE_DEVICES`, `ROCR_VISIBLE_DEVICES`

### Env Variables
| Var | Purpose |
|-----|---------|
| `OLLAMA_HOST` | API bind (default 127.0.0.1:11434) |
| `OLLAMA_MODELS` | Model storage path |
| `OLLAMA_KEEP_ALIVE` | Model RAM retention |
| `OLLAMA_DEBUG` | Verbose logging |

### References
- `man ollama`
- [Ollama Docs](https://github.com/ollama/ollama/blob/main/docs/)
- [Model Library](https://ollama.com/library)
```

---

### 2. Common-ollama-interactive-commands.md (P0)

**Issues:** Has metadata but no LOG header, good content

**Proposed Structure:**
```
LOG: [LEARN] Reference: Ollama Interactive Commands & Parameters

**Title:** Common Ollama Interactive Commands
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Common-ollama-interactive-commands.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)
### Interactive Commands
```bash
/set parameter temperature 0.7
/set parameter num_ctx 8192
/set parameter top_p 0.9
/show info
/save session-name
/load session-name
/bye
```

### Model Management
```bash
$ ollama list
$ ollama show llama3.2
$ ollama pull llama3.2:8b-instruct-q5_K_M
$ ollama rm mistral:7b
$ ollama cp llama3.2 my-llama3.2
$ ollama ps
```

### Context Length
```bash
# Interactive
/set parameter num_ctx 8192
# API
{"options": {"num_ctx": 8192}}
# Modelfile
PARAMETER num_ctx 8192
```

### Key Parameters
| Param | Values | Effect |
|-------|--------|--------|
| `temperature` | 0.2–1.0+ | Deterministic → Creative |
| `top_p` | 0.1–1.0 | Nucleus sampling |
| `top_k` | 1–100 | Top-k sampling |
| `num_predict` | -1 to N | Max output tokens |
| `stop` | ["str"] | Stop sequences |
| `repeat_penalty` | 1.0–2.0 | Repetition penalty |

### API Integration
```bash
# Generate
curl http://localhost:11434/api/generate -d '{"model":"phi4-mini","prompt":"...","stream":false}'
# Chat
curl http://localhost:11434/api/chat -d '{"model":"llama3.2","messages":[{"role":"user","content":"..."}]}'
# Embeddings
curl http://localhost:11434/api/embeddings -d '{"model":"nomic-embed-text","prompt":"..."}'

# OpenAI compatible
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```

### Model Selection Guide
| Task | Model |
|------|-------|
| Chat | llama3.2, mistral, gemma3 |
| Code | codellama, phi4, starcoder2 |
| Low RAM | phi4-mini, q4_K_M |
| Vision | llava, moondream |

### GPU Setup
| Vendor | Requirement |
|--------|-------------|
| NVIDIA | CUDA 5.0+, proprietary drivers |
| AMD | ROCm, RX 6000+ |
| Apple | Metal (auto) |

### Env Variables
| Var | Purpose |
|-----|---------|
| `OLLAMA_HOST` | Bind address (default 127.0.0.1:11434) |
| `OLLAMA_MODELS` | Model storage path |
| `OLLAMA_KEEP_ALIVE` | RAM retention (e.g., 5m, -1=forever) |
| `OLLAMA_DEBUG` | Verbose logging |

## The "Blueprint" (The Why/Logic)
### Parameter Effects
- `temperature 0.2` — deterministic, factual
- `temperature 0.7` — balanced (default)
- `temperature 1.0+` — creative, diverse
- `num_ctx` — larger = more context, more RAM
- `num_predict -1` — unlimited output

### Quantization
| Level | Size | Quality |
|-------|------|---------|
| q4_K_M | ~4GB | Good balance |
| q5_K_M | ~5GB | Better |
| q8_0 | ~8GB | Near original |

## The "Deep Dive" (The Technical Root)
### Modelfile
```dockerfile
FROM llama3.2
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
SYSTEM "You are a cybersecurity expert."
TEMPLATE "{{ if .System }}System: {{ .System }}{{ end }}User: {{ .Prompt }}Assistant: "
```

### GGUF Import
```bash
ollama create my-model -f Modelfile
# Modelfile:
FROM ./model.gguf
PARAMETER num_ctx 4096
```

### OpenAI Compatibility
```python
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
client.chat.completions.create(model="llama3.2", messages=[...])
```

### Troubleshooting
| Issue | Fix |
|-------|-----|
| Port conflict | `OLLAMA_HOST=0.0.0.0:11435` |
| GPU not detected | Update drivers, check CUDA/ROCm |
| Slow downloads | Check proxy/firewall |

### References
- [Ollama Docs](https://github.com/ollama/ollama)
- [Model Library](https://ollama.com/library)
```

---

### 3. Ollama-CLI-tricks.md (P0)

**Issues:** Missing metadata, no LOG header, good reference content

**Proposed Structure:** Similar 4-section format, expand with explanations for each trick.

---

### 4. Fabric-Fixed-Error-Analysis-And-Shell-Completion-Review.md (P1)

**Issues:** Session log content, 19 line len, 6 headers, 24 trailing, missing 1 meta, no LOG

**Key Content to Preserve:**
- 5-minute cache for dynamic completions
- Binary existence check
- Better value completions (temperature, top-p, penalties)
- Fixed _describe errors (removed helper functions)
- Root cause: conflicting completion files in `~/.zsh-completions/` vs system path
- Solution: remove broken file, let system one take over
- Cache auto-populates on first use
- `unfunction _fabric; autoload -U _fabric` to reload

**Proposed Structure:** Convert session log to structured tutorial with Recipe (steps to fix), Blueprint (why fpath order matters, cache design), Deep Dive (zsh completion architecture, _describe vs _arguments, autoload mechanism).

---

### 5. FABRIC-SOLUTION.md (P1)

**Issues:** 3 line len, 19 headers, 4 code blocks, 2 inline, 2 trailing, missing metadata, no LOG

**Content:** Complete solution for Fabric clipboard integration with niri hotkeys, shell functions, background monitor.

**Proposed Structure:** Add LOG header + metadata, reorganize into Recipe (install steps), Blueprint (why wl-clipboard, niri hotkeys, background monitor), Deep Dive (Wayland clipboard, niri IPC, PID file management, signal handling).

---

### 5. fabric-usage-guide.md (P1)

**Issues:** 1 line len, 51 headers, 17 code blocks, 9 inline, missing metadata, no LOG

**Content:** Comprehensive guide for fabric-clipboard-monitor.sh with 4 scenarios (auto, dev, one-shot, manual), systemd service, security considerations.

**Proposed Structure:** Add LOG header + metadata, reorganize scenarios into Recipe, Blueprint (why polling vs inotify, PID file locking, log rotation), Deep Dive (Wayland wl-copy/wl-paste, fabric API, signal handling, systemd user services).

---

### 6. Fabric-Clipboard-Integration-Complete-Solution.md (P1)

**Issues:** 7 headers, has metadata, no LOG

**Content:** Duplicate of FABRIC-SOLUTION.md with slight variations.

**Proposed Action:** Merge with FABRIC-SOLUTION.md, keep best content, remove duplicate.

---

### 7. PromptMaxer.md (P0)

**Issues:** 49 line len, 3 headers, 61 trailing whitespace, missing metadata, no LOG, complex prompt template

**Content:** Full prompt engineering framework with 2 modes (Return/Execute), 4-stage pipeline (Deconstruct, Diagnose, Develop, Deliver), 10 core techniques, task-type matching table.

**Proposed Structure:** Add LOG header + metadata, restructure into Recipe (activation, mode detection, pipeline), Blueprint (why 4 stages, technique matching logic), Deep Dive (prompt injection for self, continuous mode, judgment calls).

---

### 8. The-Best-ChatGPT-Prompts-Ever-Written.md (P0)

**Issues:** Missing metadata, no LOG, CRAFT prompt template

**Content:** CRAFT acronym (Context, Role, Action, Format, Target Audience) with example.

**Proposed Structure:** Add LOG header + metadata, restructure into Recipe (CRAFT sections), Blueprint (why CRAFT works, role framing, action decomposition), Deep Dive (prompt injection defense, few-shot framing, meta-guidance).

---

### 9. Advanced-Research-Assistant.md (P0)

**Issues:** 6 line len, 4 headers, missing metadata, no LOG, session log

**Content:** Web-LLM.py interactive research assistant with search, status, focus commands.

**Proposed Structure:** Add LOG header + metadata, restructure into Recipe (install, commands, research flow), Blueprint (why interactive research, status/focus/quit commands), Deep Dive (search tool integration, session management, summary generation).

---

### 10. Opencode-AI-Capabilities.md (P1)

**Issues:** 1 header, has metadata, no LOG, session log

**Content:** Brief overview of Opencode-AI models (BERT, RoBERTa, GNNs, RL). Confuses Opencode with OpenAI.

**Proposed Structure:** Add LOG header, fix content (Opencode ≠ OpenAI), restructure as reference for actual Opencode tool capabilities.

---

### 11. FHD_Prompt_BestResults_Deep-v3_1_671b_cloud.md (P1)

**Issues:** 14 headers, 19 code blocks, 10 inline, has metadata, no LOG

**Content:** Deep prompt template for DeepSeek/v3 model.

**Proposed Structure:** Add LOG header, restructure into Recipe/Blueprint/Deep Dive.

---

### 12. Opencode-run--attach-connection-to-running-server.md (P1)

**Issues:** 7 line len, 9 headers, 4 trailing, missing metadata, no LOG

**Content:** Short note about `opencode -s <session-id>`

**Proposed Structure:** Add LOG header + metadata, expand into reference with common session management commands.

---

### 13. Prompt-Rewrite-Reforge-Markdown-Files.md (P1)

**Issues:** 1 header, 1 trailing, missing metadata, no LOG

**Content:** Short note about prompt rewriting.

**Proposed Structure:** Add LOG header + metadata, expand or merge with PromptMaxer.md.

---

### 14. Common-ollama-interactive-commands.md (P0)

**Issues:** Has metadata, no LOG header

**Proposed Structure:** Add LOG header, keep content, restructure into 4-section format.

---

### 15. Ollama-CLI-tricks.md (P0)

**Issues:** Missing metadata, no LOG header

**Proposed Structure:** Add LOG header + metadata, restructure tricks into categorized reference.

---

### 16. Fabric-Clipb-Integ-Comp-Solution/Fabric-Clipboard-Integration-Complete-Solution.md (P1)

**Issues:** 7 headers, has metadata, no LOG

**Proposed Action:** Merge with FABRIC-SOLUTION.md (duplicate content), keep best version.

---

## Approval Request

Please review the above diffs. For each file, respond with:
- **APPROVE** — apply as proposed
- **MODIFY** — specify changes
- **SKIP** — don't modify this file
- **REVIEW** — need to see full corrected content first

Batch will be applied after your approval.