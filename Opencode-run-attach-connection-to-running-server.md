LOG: [LEARN] Reference: Opencode Run Attach — Connect to Running Server

**Title:** Opencode Run Attach Connection to Running Server
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Opencode-run-attach-connection-to-running-server.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Opencode installed (`npm install -g opencode-ai` or `curl -fsSL https://opencode.dev/install.sh | sh`)
- Network access to server

### Quick Start
```bash
# Terminal 1: Start server
opencode serve
# Or with web UI:
opencode web --port 4096 --hostname 0.0.0.0

# Terminal 2: Attach and run
opencode run --attach http://localhost:4096 "Your prompt here"
```

### Remote Server
```bash
opencode run --attach http://remote-host:4096 "Your prompt here"
```

### Common Options
```bash
# Specific model
opencode run --attach http://localhost:4096 --model anthropic/claude-3.5-sonnet "Prompt"

# Specific agent
opencode run --attach http://localhost:4096 --agent my-agent "Prompt"

# Continue session
opencode run --attach http://localhost:4096 --continue "Prompt"

# Specific session
opencode run --attach http://localhost:4096 --session <id> "Prompt"

# Attach file
opencode run --attach http://localhost:4096 --file ./context.txt "Prompt"

# JSON output
opencode run --attach http://localhost:4096 --format json "Prompt"
```

## The "Blueprint" (The Why/Logic)

### Why --attach?
| Benefit | Explanation |
|---------|-------------|
| **Faster execution** | Avoids cold boot on every run |
| **Consistent backend** | Same server instance, shared context |
| **Remote access** | Connect to remote servers |
| **Automation ready** | Perfect for scripts, CI/CD |

### Architecture
```
┌─────────────┐     HTTP/WS      ┌──────────────────┐
│ opencode run│◀────────────────▶│ opencode serve     │
│ --attach    │   JSON-RPC/WS    │ (MCP Server)       │
└─────────────┘                  └──────────────────┘
                                      │
                              ┌───────┴───────┐
                              ▼               ▼
                         LLM Provider    File System
                         (Anthropic,    (Your Project)
                          OpenAI, etc.)
```

### Server Modes
| Command | Description |
|---------|-------------|
| `opencode serve` | Headless MCP server (port 4096) |
| `opencode web` | Web UI + MCP server |

## The "Deep Dive" (The Technical Root)

### Protocol
- **Transport**: HTTP/WebSocket
- **Protocol**: JSON-RPC 2.0 over WebSocket
- **Auth**: None by default (local only), add reverse proxy for remote

### Connection Flow
```bash
# 1. Server starts
$ opencode serve
[INFO] MCP server listening on http://localhost:4096

# 2. Client attaches
$ opencode run --attach http://localhost:4096 "prompt"
[INFO] Connecting to http://localhost:4096
[INFO] WebSocket connected
[INFO] Executing prompt...
```

### JSON-RPC Methods
| Method | Purpose |
|--------|---------|
| `run` | Execute prompt |
| `continue` | Continue session |
| `session.list` | List sessions |
| `agent.list` | List agents |
| `model.list` | List models |

### Automation Example
```bash
#!/bin/bash
# batch-process.sh
SERVER="http://localhost:4096"

for prompt in prompts/*.txt; do
    opencode run --attach "$SERVER" --format json "$(cat "$prompt")" \
        > "output/$(basename "$prompt" .txt).json"
done
```

### Remote Access (SSH Tunnel)
```bash
# Local port forward
ssh -L 4096:localhost:4096 user@remote-host

# Then attach locally
opencode run --attach http://localhost:4096 "Prompt"
```

### Firewall/Network
```bash
# Allow local only (default)
# For remote: configure firewall + reverse proxy (nginx/caddy)
# Add TLS for production
```

### Debugging
```bash
# Verbose
opencode run --attach http://localhost:4096 --debug "Prompt"

# Check server logs
tail -f ~/.config/opencode/logs/server.log

# Test connection
curl http://localhost:4096/health
```

### References
- [Opencode GitHub](https://github.com/opencode-ai/opencode)
- [Opencode Docs](https://opencode.dev/docs)
- [MCP Specification](https://modelcontextprotocol.io/)