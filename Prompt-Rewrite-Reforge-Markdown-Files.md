LOG: [LEARN] Reference: Prompt Rewrite — Reforge Markdown Files

**Title:** Prompt Rewrite Reforge Markdown Files
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Prompt-Rewrite-Reforge-Markdown-Files.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Original Request
```bash
echo "Can you reformat the Mardown file with section titles the default line breaking column is 72 for geany editor" | fabric -sp improve_prompt
```

### Rewritten Prompt
```markdown
### Prompt Rewrite: Reforge Markdown File with Section Titles

**Line Breaking:** Set default line breaking to 72 columns in Geany Editor.
**Markdown Formatting:** Reformat the Markdown file according to standard guidelines.
```

### Usage
```bash
# Apply to any markdown file
echo "Your prompt here" | fabric -sp improve_prompt

# Or pipe file content
cat your-file.md | fabric -sp improve_prompt
```

## The "Blueprint" (The Why/Logic)

### What the Prompt Does
| Aspect | Specification |
|--------|---------------|
| **Line Breaking** | 72 columns (Geany default) |
| **Structure** | Add proper section titles |
| **Format** | Standard Markdown guidelines |

### Why 72 Columns?
- Geany editor default
- Readable in terminal (80-char width with margins)
- Git diff friendly
- Matches Markdown conventions

### Standard Markdown Guidelines
| Element | Rule |
|---------|------|
| Headers | ATX style (`# Header`) |
| Lists | `- ` or `1.` with consistent indentation |
| Code blocks | Fenced with language tags |
| Line length | ≤72 chars (prose), no limit in code |
| Links | `[text](url)` descriptive |

## The "Deep Dive" (The Technical Root)

### Geany Configuration
```ini
# ~/.config/geany/filedefs/filetypes.markdown.conf
[settings]
line_wrap=1
line_wrap_margin=72
```

### fabric improve_prompt Pattern
```bash
# The improve_prompt pattern enhances prompts by:
# 1. Adding structure (headers, sections)
# 2. Clarifying requirements
# 3. Adding constraints
# 4. Specifying output format
```

### Markdown Linting
```bash
# Install
pip install markdownlint-cli

# Check
markdownlint *.md

# Fix
markdownlint --fix *.md
```

### AGENTS.md Compliance
- 72-column line wrapping
- ATX headers (`# Header`)
- Fenced code blocks with language
- Proper metadata block
- No trailing whitespace
- Single final newline

### References
- [Geany Documentation](https://www.geany.org/doc/)
- [Markdown Guide](https://www.markdownguide.org/)
- [fabric GitHub](https://github.com/danielmiessler/fabric)
- [AGENTS.md](https://github.com/your-repo/AGENTS.md)