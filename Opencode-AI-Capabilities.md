LOG: [LEARN] Reference: Opencode — AI Coding Agent Capabilities

**Title:** Opencode AI Capabilities
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Opencode-AI-Capabilities.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### What is Opencode?
Opencode is an **AI coding agent** (not OpenAI) — a terminal-native AI assistant that operates directly in your codebase. It reads, writes, and modifies files, runs commands, and helps with software development tasks.

### Installation
```bash
# macOS/Linux
curl -fsSL https://opencode.dev/install.sh | sh

# Or via npm
npm install -g opencode-ai

# Verify
opencode --version
```

### Basic Usage
```bash
# Start in project directory
cd my-project
opencode

# Or run single command
opencode "Add error handling to auth.py"
```

### Key Capabilities
| Capability | Description |
|------------|-------------|
| **File Operations** | Read, write, edit, search files |
| **Command Execution** | Run shell commands, tests, builds |
| **Code Navigation** | Jump to definitions, find references |
| **Git Integration** | Stage, commit, diff, history |
| **Test Running** | Execute, debug, watch tests |
| **Refactoring** | Rename, extract, inline across files |

## The "Blueprint" (The Why/Logic)

### Opencode vs. OpenAI (Critical Distinction)
| Aspect | Opencode | OpenAI |
|--------|----------|--------|
| **Type** | Coding agent (CLI tool) | AI model provider (API) |
| **Interface** | Terminal-native | REST API |
| **Context** | Your entire codebase | Prompt window |
| **Actions** | Executes code, runs tests | Generates text |
| **Cost** | Local (Ollama) or API keys | Per-token billing |

### Architecture
```
User Request
    ↓
Opencode Agent
    ↓
┌─────────────────────────────────────┐
│  Tools Available                    │
├─────────────────────────────────────┤
│  read_file, write_file, edit_file   │
│  run_command, search_files          │
│  git_status, git_diff, git_commit   │
│  lsp_goto_definition, lsp_references│
└─────────────────────────────────────┘
    ↓
Executes in your project directory
```

### Model Support
| Provider | Models |
|----------|--------|
| **Ollama (local)** | llama3.2, codellama, phi4, mistral |
| **OpenAI API** | gpt-4o, gpt-4o-mini, o1 |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus |
| **OpenRouter** | 100+ models |

## The "Deep Dive" (The Technical Root)

### Session Management
```bash
# List sessions
opencode --list

# Resume session
opencode -s <session-id>

# New session
opencode
```

### Configuration
```json
// ~/.config/opencode/config.json
{
  "model": "claude-3.5-sonnet",
  "temperature": 0.2,
  "max_tokens": 8192,
  "tools": ["read", "write", "edit", "bash", "git"],
  "auto_approve": false
}
```

### Tool Definitions
```typescript
// Core tools Opencode provides
interface OpencodeTools {
  read_file(path: string): string;
  write_file(path: string, content: string): void;
  edit_file(path: string, oldStr: string, newStr: string): void;
  search_files(pattern: string): string[];
  run_command(cmd: string): { stdout: string; stderr: string; code: number };
  git_status(): GitStatus;
  git_diff(): string;
  git_commit(msg: string): void;
  lsp_goto_definition(symbol: string): Location;
  lsp_references(symbol: string): Location[];
}
```

### Workflow Patterns
| Pattern | Use Case |
|---------|----------|
| **Explore → Plan → Execute** | New features, refactoring |
| **Test → Fix → Verify** | Bug fixing |
| **Read → Understand → Modify** | Code review, learning |
| **Search → Analyze → Refactor** | Technical debt |

### References
- [Opencode GitHub](https://github.com/opencode-ai/opencode)
- [Opencode Docs](https://opencode.dev/docs)
- [Model Configuration](https://opencode.dev/docs/models)