LOG: [LEARN] Reference: Ollama CLI Tricks & Patterns

**Title:** Ollama CLI Tricks
**Date:** 2026-02-09 (22:27:16 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Ollama-CLI-tricks.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Input from Stdin
```bash
$ ollama run llama3.1 "prompt"
```

### Multiline Input
```bash
$ ollama run llama3.1 """
Multi-line
prompt here
"""
```

### Input from File
```bash
# Pipe operator
$ cat fox.txt | ollama run llama3.1 "Translate to German"
# Redirection operator
$ ollama run llama3.1 "Translate to German" < fox.txt
```

### Consuming Web Pages
```bash
$ curl -s https://lite.cnn.com/.../index.html | ollama run llama3.1 "Summarize this HTML"
$ curl -s https://lite.cnn.com/.../index.html | ollama run llama3.1 "Find all people names"
```

### Chaining LLMs (Pipe Output)
```bash
$ ollama run llama3.1 "How do you make scrambled eggs?" | ollama run llama3.1 "Translate to German"
```

### Output to File
```bash
# JSON output
$ ollama run llama3.1 "Countries of Europe" --format json > europe.json

# Append to file
$ ollama run llama3 "Tell me a joke about programming" > jokes.md
$ ollama run llama3 "Tell me a joke about programming" >> jokes.md
```

### Verbose Output
```bash
$ ollama run llama3.1 --verbose "What is the capital of Iceland?"
```

## The "Blueprint" (The Why/Logic)

### Input Methods
| Method | Syntax | Use Case |
|--------|--------|----------|
| Direct prompt | `ollama run model "prompt"` | Simple queries |
| Stdin pipe | `cat file \| ollama run model "prompt"` | File + instruction |
| Redirection | `ollama run model "prompt" < file` | File as context |
| Heredoc | `ollama run model <<'EOF' ... EOF` | Multi-line prompts |

### Chaining Strategy
- Output of model A → Input to model B
- Useful for: translate → summarize, generate → format, code → explain
- Each hop adds latency; prefer single model when possible

### Output Formats
| Flag | Format | Use Case |
|------|--------|----------|
| `--format json` | JSON | Programmatic parsing |
| `--format text` | Plain text | Default |
| `> file` | Redirect | Save output |
| `>> file` | Append | Accumulate output |

## The "Deep Dive" (The Technical Root)

### Streaming vs Non-Streaming
```bash
# Streaming (default)
$ ollama run llama3.1 "prompt"

# Non-streaming (complete response)
$ ollama run llama3.1 "prompt" --stream false
```

### Verbose Mode
```bash
$ ollama run llama3.1 --verbose "prompt"
# Shows: model load time, token count, eval rate
```

### Format Options
```bash
$ ollama run llama3.1 "List countries" --format json
# {"countries": ["Austria", "Belgium", ...]}

$ ollama run llama3.1 "Code" --format text
```

### File I/O Patterns
```bash
# Read file as context
$ ollama run llama3.2 "Summarize" < long-doc.txt

# Save response
$ ollama run llama3.2 "Prompt" > output.txt

# Append to log
$ ollama run llama3.2 "Prompt" >> session.log

# JSON + file
$ ollama run llama3.1 "Data" --format json > data.json
```

### Web Scraping + LLM
```bash
# Use text-mode sites (lite.cnn.com, textise.net)
$ curl -s https://lite.cnn.com/article.html | ollama run llama3.1 "Summarize"

# Extract specific info
$ curl -s https://example.com | ollama run llama3.1 "Extract all email addresses"
```

### References
- `man ollama`
- [Ollama GitHub](https://github.com/ollama/ollama)