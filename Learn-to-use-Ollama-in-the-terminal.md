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