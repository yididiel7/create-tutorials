#!/usr/bin/env python3
"""
Fix common markdown compliance issues in tutorial files.
"""

import re
from pathlib import Path

ROOT = Path("/home/srhills/labs/experiments/create-tutorials")

def fix_file(content: str) -> str:
    """Apply common fixes to markdown content."""
    
    # 1. Fix code block indentation - remove leading spaces from ``` lines
    lines = content.splitlines()
    fixed_lines = []
    in_code_block = False
    for line in lines:
        if line.lstrip().startswith("```"):
            # Remove leading whitespace from fence lines
            fixed_lines.append(line.lstrip())
            in_code_block = not in_code_block
        else:
            fixed_lines.append(line)
    content = "\n".join(fixed_lines)
    
    # 2. Ensure code blocks have language tags (default to bash for shell commands)
    def add_lang_tag(match):
        fence = match.group(0)
        if fence.strip() == "```" and not in_code_block:
            return "```bash"
        return fence
    
    # This is tricky - need to track state. Simpler: post-process
    lines = content.splitlines()
    fixed_lines = []
    in_code_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code_block and stripped == "```":
                # Opening fence without language
                fixed_lines.append("```bash")
            else:
                fixed_lines.append(line)
            in_code_block = not in_code_block
        else:
            fixed_lines.append(line)
    content = "\n".join(fixed_lines)
    
    # 3. Fix header case: H1 Title Case, H2+ Sentence case
    def fix_header_case(match):
        level = len(match.group(1))
        text = match.group(2).strip()
        if level == 1:
            # Title Case
            words = text.split()
            fixed = " ".join(w.capitalize() if w.lower() not in 
                           ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by', 'in', 'of', 'with'] 
                           else w.lower() for w in words)
        else:
            # Sentence case
            fixed = text.capitalize()
        return f"{'#' * level} {fixed}"
    
    content = re.sub(r"^(#{1,6})\s+(.+)$", fix_header_case, content, flags=re.MULTILINE)
    
    # 4. Fix inline code spacing: ` text ` -> `text`
    content = re.sub(r"`\s+([^`\n]+?)\s+`", r"`\1`", content)
    
    # 5. Wrap long lines at 72 chars (outside code blocks)
    lines = content.splitlines()
    fixed_lines = []
    in_code_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            fixed_lines.append(line)
        elif not in_code_block and len(line) > 72:
            # Simple wrap at word boundary
            words = line.split()
            wrapped = []
            current = ""
            for word in words:
                if len(current) + len(word) + 1 <= 72:
                    current = (current + " " + word).strip()
                else:
                    if current:
                        wrapped.append(current)
                    current = word
            if current:
                wrapped.append(current)
            fixed_lines.extend(wrapped)
        else:
            fixed_lines.append(line)
    content = "\n".join(fixed_lines)
    
    # 6. Ensure final newline
    if not content.endswith("\n"):
        content += "\n"
    elif content.endswith("\n\n"):
        content = content.rstrip("\n") + "\n"
    
    return content

# Test on one file
with open(ROOT / "Beginner_Tutorial_Arch0_Intro_CLI.md") as f:
    original = f.read()

fixed = fix_file(original)
print("=== FIXED ===")
print(fixed[:2000])