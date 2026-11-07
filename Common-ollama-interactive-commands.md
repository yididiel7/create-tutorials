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