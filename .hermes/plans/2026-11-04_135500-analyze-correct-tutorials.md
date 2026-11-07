# Plan: Analyze & Correct All Tutorial Files (Content, Structure, Syntax)

**Date:** 2026-11-04
**Goal:** Systematically read, analyze, and fix all 164 markdown files for: misleading/incorrect content, header formatting, Markdown professional structure, syntax errors, and AGENTS.md compliance — with review checkpoints before committing.

---

## Current Context / Assumptions

- **Root directory:** `/home/srhills/labs/experiments/create-tutorials` (164 `.md` files + subdirs)
- **Organization plan** already created (12 categories, `INDEX.md` navigation)
- **AGENTS.md standards** are the authority: 72-col lines, ATX headers, metadata blocks, fenced code blocks, Title-Case filenames
- **User wants:** Review corrected files before any commits — no blind changes
- **Scope:** Content accuracy + structural compliance + syntax hygiene

---

## Tutorial File Structure Standard (User-Defined)

All tutorial files (P0/P1) will follow this **four-section structure** with a grep-friendly header:

### 1. The Header (DAO) — Grep Target
```markdown
LOG: [LEARN] Understanding: [Topic Name]
```
- Domain tag `[LEARN]` enables instant `grep -r "LOG: \[LEARN\]" .`
- `Understanding:` prefix indicates tutorial type (could be `Reference:`, `Guide:`, `Debug:`)
- Topic Name = human-readable title matching filename

### 2. The "Recipe" (The How)
- Step-by-step procedural instructions
- Commands with prompts (`$` user, `#` root)
- Expected output examples
- Prerequisites listed first

### 3. The "Blueprint" (The Why/Logic)
- Conceptual explanation of *why* steps work
- Architecture/design decisions
- Common pitfalls and alternatives
- Mental models

### 4. The "Deep Dive" (The Technical Root)
- Technical internals, edge cases, version specifics
- Advanced configuration
- Troubleshooting/debugging details
- References to source docs (Arch Wiki, man pages, upstream)

---

**Metadata Block (retained for AGENTS.md compliance):**
```markdown
**Title:** Human Readable Title
**Date:** YYYY-MM-DD (HH:MM:SS TIMEZONE)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** filename.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details
```
Placed *after* the LOG header, before Section 2.

---

**Example Complete Tutorial Template:**
```markdown
LOG: [LEARN] Understanding: Configure Nginx Virtual Hosts

**Title:** How to Configure Nginx Virtual Hosts
**Date:** 2026-11-04 (14:30:00 IST)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** Configure-Nginx-Virtual-Hosts.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Nginx installed
- Root/sudo access

### Steps
1. Create site config...
   ```bash
   $ sudo vim /etc/nginx/sites-available/example.com
   ```

## The "Blueprint" (The Why/Logic)

Nginx uses server blocks to...

## The "Deep Dive" (The Technical Root)

The `server_name` directive...
```

---

## Architecture / Proposed Approach

**Three-phase pipeline with review gates:**

1. **Phase 1 — Automated Audit (fast, no LLM):** Run markdownlint, link checker, metadata validator across all files. Produce a machine-readable report of every violation.
2. **Phase 2 — Targeted Content Review (LLM-assisted, batched):** For files flagged by Phase 1 + high-priority files (tutorials, not sessions/logs), read content, verify commands, fix headers/metadata/structure, correct misleading info. Output: diff per file.
3. **Phase 3 — Review & Commit:** Present diffs grouped by category for your approval. Apply only approved changes.

**Batching strategy:** Process by category directory (from organization plan), ~15–25 files per batch. Each batch = one review checkpoint.

**Tooling:**
- `markdownlint` (or custom Python) for syntax/structure
- `lychee` or custom for broken links
- Custom script to validate AGENTS.md metadata block presence/format
- LLM read + patch for content corrections

---

## Step-by-Step Tasks

### Task 1: Set Up Audit Tooling
```bash
cd /home/srhills/labs/experiments/create-tutorials
# Check available tools
which markdownlint lychee
# If missing, install via uv (preferred) or npm/pip
uv tool install markdownlint-cli  # or: uv pip install markdownlint-cli
uv tool install lychee             # or: uv pip install lychee
# Create audit script: scripts/audit_markdown.py
```

**Deliverable:** `audit_report.json` with per-file violations:
- Line length >72
- Missing/invalid metadata block (Title, Date, Author, lfnc, Copyright, License)
- Header style (Setext vs ATX, case consistency)
- Code block language tags
- Trailing whitespace, missing final newline
- Broken internal/external links
- Inline code spacing violations

---

### Task 2: Run Full Automated Audit
```bash
python scripts/audit_markdown.py --root . --output audit_report.json
```

**Output:** JSON with structure:
```json
{
  "files": {
    "Arch-Linux/Arch_Linux_command-line_commands.md": {
      "line_length": [{"line": 45, "length": 89}],
      "metadata": {"missing": ["lfnc", "License"]},
      "headers": [{"line": 1, "issue": "Setext style"}],
      "code_blocks": [{"line": 12, "issue": "missing language tag"}],
      "links": [{"line": 30, "url": "http://example.com", "status": "broken"}]
    },
    ...
  },
  "summary": {"total_files": 164, "files_with_issues": 142, "total_violations": 1247}
}
```

---

### Task 3: Prioritize Files for Content Review
**Classification (from audit + manual triage):**

| Priority | Criteria | Est. Count |
|----------|----------|------------|
| **P0 — Tutorials** | Has metadata block, teaches a procedure, user-facing | ~60 |
| **P1 — References** | Cheatsheets, command references, config guides | ~30 |
| **P2 — Session/Debug** | `session-ses_*.md`, `copilot-session-*.md`, `*Analysis*.md` | ~25 |
| **P3 — Personal/Meta** | `Psychological-Profile*.md`, `TELOS*.md`, `MY_TELOS_FILE.md`, `politics-and-quotes.md` | ~15 |
| **P4 — Duplicates/Near-dupes** | `create_prompt_tutorial.md` vs `create_prompt_tutorial_1.md`, `uv-python-manager.md` vs `uv-python-package-manager.md` | ~10 |
| **P5 — Non-tutorial** | `.lua`, `.sh`, `.bak`, `.aux`, `.log`, `.tex` files | ~14 |

**Decision:** Only P0 + P1 get full content review (commands verified, misleading info corrected). P2–P5 get structural fixes only (metadata, line breaks, syntax).

---

### Task 4: Batch Content Review — Category by Category
For each category directory (from organization plan), process P0/P1 files:

**Sub-task 4.x per file:**
1. Read file content
2. Verify every shell command works on Arch Linux (dry-run or known-good)
3. Check for misleading/incorrect claims (version-specific flags, deprecated syntax)
4. **Restructure to four-section format:**
   - Ensure `LOG: [LEARN] Understanding: [Topic Name]` header exists
   - Reorganize content into: **Recipe** (How) → **Blueprint** (Why) → **Deep Dive** (Technical Root)
   - Preserve metadata block (Title, Date, Author, lfnc, Copyright, License) after LOG header
5. Convert Setext → ATX headers, fix case (Title Case main, Sentence case sub)
6. Wrap lines at 72 cols (preserve code blocks, tables)
7. Add language tags to all fenced code blocks
8. Fix inline code spacing (no spaces inside backticks)
9. Fix link text to be descriptive (not "click here")
10. Generate unified diff

**Output per batch:** `review_batch_<category>.md` containing:
- File list processed
- For each file: original → corrected diff (unified format)
- Summary of content corrections made (commands fixed, claims corrected)

**Batch order (matches organization plan):**
1. `Arch-Linux/` (~18 files, mostly P0)
2. `Terminal-Shell/` (~19 files, mostly P0/P1)
3. `Editors-IDEs/` (~24 files, mostly P0/P1)
4. `AI-ML-Tools/` (~16 files, mixed)
5. `Network/` (~4 + subdir, P0/P1)
6. `System-Utilities/` (~10 files, P0)
7. `Development-Tools/` (~16 files, mixed)
8. `Window-Managers/` (~8 files, P0)
9. `Desktop-UI/` (~7 files, P1)
10. `File-Managers/` (2 files, P0)
11. `Meta-Reference/` (P0/P1 only ~10, rest structural only)
12. `Virtualization/`, `Security/` (minimal)

---

### Task 5: Structural-Only Fixes for P2–P5
For session/log/personal files:
- Add minimal metadata block (Title, Date, lfnc)
- Wrap lines at 72 cols
- Fix syntax (code blocks, headers)
- No content verification

**Output:** `review_batch_structural.md` with diffs.

---

### Task 6: Deduplication Analysis
For P4 near-duplicates:
- `create_prompt_tutorial.md` vs `create_prompt_tutorial_1.md`
- `uv-python-manager.md` vs `uv-python-package-manager.md` vs `UV_how_to_Install_uv.md`
- `Nmcli-a-Powerful-Command-line-tool.md` (root) vs `Network/Nm-Arch-Guide/Nmcli-a-Powerful-Command-line-tool.md`
- `chat-📄-Refactoring-Markdown-Instructions.md` vs `refactor_markdown_prompt.md` vs `Prompt-Rewrite-Reforge-Markdown-Files.md`

**Action:** Compare content, recommend merge/rename/delete. Present for decision.

---

### Task 7: Review Checkpoints (User Gates)
After each batch (Tasks 4.1–4.12, 5, 6):
1. Present `review_batch_<name>.md` with all diffs
2. You approve / reject / modify per file
3. Approved diffs → apply with `patch`
4. Run audit again on changed files to verify clean
5. Commit (if git) or stage for final commit

**Format for your review:**
```markdown
## Batch: Arch-Linux

### Arch-Linux/Arch_Linux_command-line_commands.md
**Changes:** Metadata block added, 3 commands corrected (pacman -Syu → pacman -Syyu), 12 lines wrapped, 2 code blocks tagged `bash`
**Diff:**
```diff
- **Title:** Arch Linux Commands
+ **Title:** Arch Linux Command-Line Commands
+ **Date:** 2026-02-13
+ **Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
+ **lfnc:** Arch_Linux_command-line_commands.md
+ **Copyright:** © 2026-2027 Sr. Tyrone Hills
+ **License:** MIT – see LICENSE file for details
...
- $ pacman -Syu package
+ $ pacman -Syyu package  # Force refresh databases
```

---

### Task 8: Final Validation & INDEX.md Generation
```bash
# Re-run full audit — zero violations expected
python scripts/audit_markdown.py --root . --output final_audit.json

# Generate INDEX.md from organized structure
python scripts/generate_index.py --root . --output INDEX.md
```

---

## Tests / Validation

| Check | Command | Expected |
|-------|---------|----------|
| Zero markdownlint errors | `markdownlint **/*.md` | Exit 0 |
| Zero broken links | `lychee **/*.md` | All OK |
| All P0/P1 files have metadata | `grep -L "lfnc:" P0_P1_files` | Empty |
| All P0/P1 files have LOG header | `grep -L "LOG: \[LEARN\]" P0_P1_files` | Empty |
| All code blocks tagged | `grep -r '^```$' **/*.md` | Empty |
| Lines ≤72 cols (excl. code) | `awk 'length>72 && !/^```/' **/*.md` | Empty |
| File count unchanged | `find . -name "*.md" | wc -l` | 164 |

---

## Risks, Tradeoffs, Open Questions

| Risk / Question | Mitigation / Decision |
|----------------|------------------------|
| **164 files × manual review = huge time** | Batch by category; you review diffs, not raw files. Only P0/P1 get content review (~90 files). |
| **Command verification on Arch** | Dry-run in container or check against Arch Wiki / man pages. No live execution without approval. |
| **Subjective "misleading" claims** | Flag uncertain items in diff with `> **Note:** Uncertain — verify: ...` for your decision. |
| **Session files are huge** (e.g., `QS-Inst-Analysis-SUMMARY-session-ses_3c11.md` = 293KB) | Structural fixes only. No content review. Optionally truncate/archive. |
| **Non-ASCII filenames** (`Creating-Custom-Fabric-Patterns-✂️.md`) | Keep as-is; AGENTS.md allows Title-Case-With-Dashes. Emoji in filename is edge case — rename to `Creating-Custom-Fabric-Patterns.md`? |
| **Duplicate files** | Task 6 handles. You decide merge strategy. |
| **AGENTS.md itself needs fixes** | It's in Meta-Reference; will be audited like any file. |
| **Git history** | If repo has git, commit per batch. If not, changes are staged for final commit. |

---

## Deliverables for Your Review

1. **`audit_report.json`** — complete machine audit (Task 2)
2. **12 `review_batch_<category>.md`** — content + structural diffs for P0/P1 (Tasks 4.1–4.12)
3. **`review_batch_structural.md`** — structural diffs for P2–P5 (Task 5)
4. **`review_deduplication.md`** — duplicate analysis with recommendations (Task 6)
5. **`final_audit.json`** — clean bill of health (Task 8)
6. **`INDEX.md`** — navigation index (Task 8)

---

## Plan Saved To
`.hermes/plans/2026-11-04_135500-analyze-correct-tutorials.md`