LOG: [LEARN] Guide: Web-LLM.py Interactive Research Assistant

**Title:** Advanced Research Assistant
**Date:** 2026-02-11 (17:46:18 IST)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Advanced-Research-Assistant.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Python 3.10+
- `uv` package manager (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Internet connection

### Installation
```bash
# Clone or create Web-LLM.py
git clone <repo>  # or create from source

# Install dependencies
uv sync

# Or run directly
uv run Web-LLM.py
```

### Usage Modes

#### Interactive Research Mode
```bash
$ uv run Web-LLM.py

    ╔═══════════════════════════════════════════════════════════╗
    ║             🌐 Advanced Research Assistant 🤖             ║
    ╚═══════════════════════════════════════════════════════════╝

    Welcome to the Advanced Research Assistant!

    Usage:
    - Start your research query with '@'
      Example: "@analyze the impact of AI on healthcare"

    Press CTRL+D (Linux/Mac) or CTRL+Z (Windows) to submit input.
```

#### Direct Tool Usage (Programmatic)
```python
# Built-in search tools available:
websearch("latest AI breakthroughs 2026")
webfetch("https://example.com/article")
codesearch("python async pattern")
google_search("AI healthcare 2026")
```

### Research Commands (Interactive)
| Command | Action |
|---------|--------|
| `s` | Show research status |
| `f` | Show current focus |
| `q` | Quit research |

### Research Flow
```
1. Enter query with @ prefix
2. System initiates research
3. Runs searches, fetches pages
4. Generates summary
5. Shows available commands
```

## The "Blueprint" (The Why/Logic)

### Architecture
```
User Query (@query)
    ↓
Query Parser
    ↓
Search Strategy (websearch/codesearch/google_search)
    ↓
Parallel Fetching (webfetch)
    ↓
Content Extraction & Summarization
    ↓
Research Summary Generation
    ↓
Interactive Commands (s/f/q)
```

### Search Tools
| Tool | Purpose |
|------|---------|
| `websearch()` | General web search |
| `webfetch()` | Fetch specific URL content |
| `codesearch()` | Code/examples search |
| `google_search()` | Google search API |

### Two Usage Paradigms
| Mode | Use Case |
|------|----------|
| **Interactive** | Exploratory research, iterative refinement |
| **Programmatic** | Automation, scripts, pipelines |

## The "Deep Dive" (The Technical Root)

### Query Processing
```
@analyze the impact of AI on healthcare
    ↓
1. Parse: extract topic "AI healthcare impact"
2. Strategy: websearch + webfetch
3. Execute: parallel searches
4. Synthesize: summary + citations
5. Present: summary + commands
```

### Rate Limiting Handling
- DuckDuckGo API rate limits → fallback to direct tools
- Built-in: `websearch()`, `webfetch()`, `codesearch()`
- Programmatic access bypasses interactive limits

### Research Summary Output
```
================================================================================
                RESEARCH SUMMARY
================================================================================
Original Query: analyze the impact of AI on healthcare
Generated on: 2026-02-11 17:46:18
[...synthesized findings...]
================================================================================
                End of Summary
================================================================================
```

### Conversation Mode
```
Instructions:
- Type question + CTRL+D to submit
- 'quit' + CTRL+D to exit
- User messages: green
- AI responses: cyan
```

### Configuration
```bash
# Environment variables
export DDG_RATE_LIMIT_DELAY=2
export WEB_FETCH_TIMEOUT=30

# Custom search engines
export SEARCH_ENGINES="duckduckgo,google,bing"
```

### References
- [uv package manager](https://docs.astral.sh/uv/)
- [DuckDuckGo HTML](https://html.duckduckgo.com/)
- [Python requests](https://docs.python-requests.org/)