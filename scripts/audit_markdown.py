#!/usr/bin/env python3
"""
Markdown Audit Script for Tutorial Files
Checks: line length, metadata blocks, headers, code blocks, links, inline code spacing
"""

import os
import re
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path("/home/srhills/labs/experiments/create-tutorials")

# AGENTS.md required metadata fields
REQUIRED_METADATA = ["Title", "Date", "Author", "lfnc", "Copyright", "License"]

# Header patterns
SETEXT_H1 = re.compile(r"^.+\n=+$", re.MULTILINE)
SETEXT_H2 = re.compile(r"^.+\n-+$", re.MULTILINE)
ATX_HEADER = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

# Metadata pattern (bold key: value)
META_PATTERN = re.compile(r"^\*\*(Title|Date|Author|lfnc|Copyright|License):\*\*\s*(.+)$", re.MULTILINE)

# Code block pattern
CODE_BLOCK = re.compile(r"^```(\w*)\n", re.MULTILINE)

# Inline code with spaces
INLINE_CODE_SPACES = re.compile(r"`\s+.+\s+`")

# Links
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def check_line_length(content: str, filepath: Path) -> List[Dict]:
    """Check for lines > 72 chars (excluding code blocks)."""
    violations = []
    in_code_block = False
    for i, line in enumerate(content.splitlines(), 1):
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if not in_code_block and len(line) > 72:
            violations.append({"line": i, "length": len(line), "content": line[:100]})
    return violations

def check_metadata(content: str, filepath: Path) -> Dict[str, Any]:
    """Check for required metadata block."""
    found = {}
    for match in META_PATTERN.finditer(content):
        found[match.group(1)] = match.group(2).strip()
    
    missing = [field for field in REQUIRED_METADATA if field not in found]
    return {
        "found": found,
        "missing": missing,
        "has_metadata_block": len(found) > 0
    }

def check_headers(content: str, filepath: Path) -> List[Dict]:
    """Check header style (Setext vs ATX) and case."""
    violations = []
    
    # Check for Setext headers
    for match in SETEXT_H1.finditer(content):
        line_no = content[:match.start()].count('\n') + 1
        violations.append({"line": line_no, "issue": "Setext H1", "style": "setext"})
    for match in SETEXT_H2.finditer(content):
        line_no = content[:match.start()].count('\n') + 1
        violations.append({"line": line_no, "issue": "Setext H2", "style": "setext"})
    
    # Check ATX header case
    for match in ATX_HEADER.finditer(content):
        level = len(match.group(1))
        text = match.group(2).strip()
        line_no = content[:match.start()].count('\n') + 1
        
        if level == 1:
            # Main header should be Title Case
            if text != text.title() and not text.isupper():
                violations.append({"line": line_no, "issue": "H1 not Title Case", "text": text})
        elif level >= 2:
            # Subheaders should be Sentence case
            if text != text.capitalize() and not text.isupper():
                violations.append({"line": line_no, "issue": f"H{level} not Sentence case", "text": text})
    
    return violations

def check_code_blocks(content: str, filepath: Path) -> List[Dict]:
    """Check for missing language tags on fenced code blocks."""
    violations = []
    for match in CODE_BLOCK.finditer(content):
        lang = match.group(1)
        line_no = content[:match.start()].count('\n') + 1
        if not lang:
            violations.append({"line": line_no, "issue": "missing language tag"})
    return violations

def check_inline_code_spacing(content: str, filepath: Path) -> List[Dict]:
    """Check for spaces inside inline code backticks."""
    violations = []
    for match in INLINE_CODE_SPACES.finditer(content):
        line_no = content[:match.start()].count('\n') + 1
        violations.append({"line": line_no, "issue": "spaces inside backticks", "content": match.group(0)[:50]})
    return violations

def check_links(content: str, filepath: Path) -> List[Dict]:
    """Extract all links for external verification."""
    links = []
    for match in LINK_PATTERN.finditer(content):
        text = match.group(1)
        url = match.group(2)
        line_no = content[:match.start()].count('\n') + 1
        links.append({"line": line_no, "text": text, "url": url})
    return links

def check_log_header(content: str, filepath: Path) -> Dict:
    """Check for LOG: [LEARN] header."""
    has_log = bool(re.search(r"LOG:\s*\[LEARN\]", content))
    log_match = re.search(r"LOG:\s*\[LEARN\]\s*(\w+):\s*(.+)", content)
    return {
        "has_log_header": has_log,
        "log_type": log_match.group(1) if log_match else None,
        "log_topic": log_match.group(2).strip() if log_match else None
    }

def check_trailing_whitespace(content: str) -> List[Dict]:
    """Check for trailing whitespace."""
    violations = []
    for i, line in enumerate(content.splitlines(), 1):
        if line.endswith(" ") or line.endswith("\t"):
            violations.append({"line": i, "issue": "trailing whitespace"})
    return violations

def check_final_newline(content: str) -> bool:
    """Check if file ends with single newline."""
    return content.endswith("\n") and not content.endswith("\n\n")

def run_markdownlint(filepath: Path) -> List[Dict]:
    """Run markdownlint on a file."""
    try:
        result = subprocess.run(
            ["markdownlint", str(filepath)],
            capture_output=True, text=True, timeout=30
        )
        violations = []
        for line in result.stdout.strip().split("\n"):
            if line and ":" in line:
                parts = line.split(":", 2)
                if len(parts) >= 3:
                    violations.append({
                        "line": int(parts[1]),
                        "rule": parts[2].strip() if len(parts) > 2 else "",
                        "message": parts[3].strip() if len(parts) > 3 else ""
                    })
        return violations
    except Exception as e:
        return [{"error": str(e)}]

def audit_file(filepath: Path) -> Dict[str, Any]:
    """Audit a single markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": f"Failed to read: {e}"}
    
    rel_path = filepath.relative_to(ROOT)
    
    return {
        "file": str(rel_path),
        "line_length": check_line_length(content, filepath),
        "metadata": check_metadata(content, filepath),
        "headers": check_headers(content, filepath),
        "code_blocks": check_code_blocks(content, filepath),
        "inline_code_spacing": check_inline_code_spacing(content, filepath),
        "links": check_links(content, filepath),
        "log_header": check_log_header(content, filepath),
        "trailing_whitespace": check_trailing_whitespace(content),
        "final_newline": check_final_newline(content),
        "markdownlint": run_markdownlint(filepath)
    }

def main():
    # Find all .md files
    md_files = list(ROOT.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    results = {
        "files": {},
        "summary": {
            "total_files": len(md_files),
            "files_with_issues": 0,
            "total_violations": 0
        }
    }
    
    for i, filepath in enumerate(md_files, 1):
        if i % 20 == 0:
            print(f"  Processed {i}/{len(md_files)}...")
        audit = audit_file(filepath)
        results["files"][str(filepath.relative_to(ROOT))] = audit
        
        # Count violations
        violation_count = 0
        for key, val in audit.items():
            if key in ["file", "metadata", "log_header", "final_newline"]:
                continue
            if isinstance(val, list):
                violation_count += len(val)
            elif isinstance(val, dict) and "missing" in val:
                violation_count += len(val["missing"])
        
        if violation_count > 0 or audit.get("metadata", {}).get("missing") or not audit.get("final_newline", True):
            results["summary"]["files_with_issues"] += 1
        results["summary"]["total_violations"] += violation_count
    
    # Save report
    output_path = ROOT / "audit_report.json"
    output_path.write_text(json.dumps(results, indent=2))
    print(f"\nAudit complete. Report saved to {output_path}")
    print(f"Files with issues: {results['summary']['files_with_issues']}/{results['summary']['total_files']}")
    print(f"Total violations: {results['summary']['total_violations']}")
    
    # Print summary by category
    print("\n--- Top Issues ---")
    issue_types = {}
    for audit in results["files"].values():
        for key in ["line_length", "headers", "code_blocks", "inline_code_spacing", "trailing_whitespace"]:
            if audit.get(key):
                issue_types[key] = issue_types.get(key, 0) + len(audit[key])
        if audit.get("metadata", {}).get("missing"):
            issue_types["missing_metadata"] = issue_types.get("missing_metadata", 0) + len(audit["metadata"]["missing"])
        if not audit.get("final_newline", True):
            issue_types["missing_final_newline"] = issue_types.get("missing_final_newline", 0) + 1
        if not audit.get("log_header", {}).get("has_log_header"):
            issue_types["missing_log_header"] = issue_types.get("missing_log_header", 0) + 1
    
    for issue, count in sorted(issue_types.items(), key=lambda x: -x[1]):
        print(f"  {issue}: {count}")

if __name__ == "__main__":
    main()