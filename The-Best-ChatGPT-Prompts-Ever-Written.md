LOG: [LEARN] Reference: CRAFT Prompt Framework for LLM Prompt Engineering

**Title:** The Best ChatGPT Prompts Ever Written — CRAFT Framework
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** The-Best-ChatGPT-Prompts-Ever-Written.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### CRAFT Acronym Framework
Use **C.R.A.F.T.** to structure high-quality LLM prompts:

| Letter | Section | Purpose |
|--------|---------|---------|
| **C** | **Context** | Situation, background, why this prompt exists |
| **R** | **Role** | Expert identity, 20+ years experience, thought leadership |
| **A** | **Action** | Numbered sequential steps for the LLM to follow |
| **F** | **Format** | Output structure: essay, table, code, markdown, list, etc. |
| **T** | **Target Audience** | Demographics, language, reading level, preferences |

### CRAFT Template
```markdown
**Context:**
[Describe the situation, background, and why this prompt is needed.
What knowledge/expertise should the LLM reference?]

**Role:**
[Define the LLM's persona: expert type, 20+ years experience,
specialization, writing style, tone]

**Action:**
1. [First sequential step]
2. [Second step]
3. [Continue with clear, actionable steps...]

**Format:**
[Specify output structure: essay, table, code, markdown, list, summary, etc.
Include details: headings, lists, examples, case studies]

**Target Audience:**
[Demographics, geography, language, reading level, preferences,
expertise level, goals]
```

### Example: Monthly Goals Guide
```markdown
**Context:**
Create a detailed guide to help individuals set, track, and achieve
monthly goals. Break down larger objectives into manageable, actionable
steps aligned with yearly vision. Focus on consistency, overcoming
obstacles, celebrating progress using SMART goals.

**Role:**
Expert productivity coach with 20+ years experience helping individuals
optimize time, define goals, achieve sustained success. Skilled in habit
formation, motivational strategies, practical planning. Clear,
motivating, actionable writing style.

**Action:**
1. Engaging intro: why monthly goals work for personal/professional growth
2. Step-by-step: breaking annual goals into monthly objectives
3. Strategies for identifying monthly priorities
4. Techniques for focus, tracking, plan adjustment
5. Examples: health, career, finances, personal development
6. Obstacles (procrastination, challenges) and solutions
7. Motivational conclusion: reflection and continuous improvement

**Format:**
Plain text, clear headings/subheadings, numbered/bulleted lists,
practical examples, case studies

**Target Audience:**
Working professionals/entrepreneurs 25-55 seeking productivity strategies.
Self-motivated, value structure/clarity. 6th grade reading level.
```

## The "Blueprint" (The Why/Logic)

### Why CRAFT Works
| Component | Purpose |
|-----------|---------|
| **Context** | Grounds LLM in relevant knowledge domain |
| **Role** | Activates expert-level knowledge patterns |
| **Action** | Provides executable, sequential instructions |
| **Format** | Constrains output to usable structure |
| **Target Audience** | Calibrates tone, complexity, vocabulary |

### Design Principles
| Principle | Application |
|-----------|-------------|
| **Sequential steps** | LLMs execute ordered instructions better |
| **Explicit role** | Activates domain-specific training patterns |
| **Concrete format** | Prevents rambling, ensures usability |
| **Audience awareness** | Calibrates vocabulary, depth, tone |

## The "Deep Dive" (The Technical Root)

### CRAFT vs. Standard Prompting
| Standard | CRAFT |
|----------|-------|
| "Write a guide on monthly goals" | Full CRAFT template above |
| Implicit context | Explicit context |
| Generic role | 20-year expert persona |
| Vague output | Structured format spec |
| Unknown audience | 6th grade, professionals 25-55 |

### CRAFT as Meta-Prompt
```markdown
# Meta-Prompt: Generate CRAFT Prompt
CONTEXT: We are creating a CRAFT prompt for [TOPIC].
ROLE: You are a prompt engineering expert.
ACTION:
1. Ask user for topic if not provided
2. Generate all 5 CRAFT sections
3. Include fill-in-the-blank placeholders
4. Output complete CRAFT-formatted prompt
FORMAT: CRAFT template (above)
TARGET: ChatGPT-4o / o1
```

### Prompt Injection Defense
CRAFT's explicit structure reduces injection risk:
- Explicit role bounds behavior
- Action steps constrain execution flow
- Format constraints limit output space
- Audience constraints limit style drift

## The "Deep Dive" (The Technical Root)

### LLM Training Alignment
| CRAFT Element | Training Pattern |
|---------------|------------------|
| Role | System prompt conditioning |
| Action | Instruction-following (RLHF) |
| Format | Structured output training |
| Context | In-context learning |

### CRAFT Prompt Quality Checklist
- [ ] Context explains *why* and *what knowledge to use*
- [ ] Role specifies *expertise level* and *writing style*
- [ ] Action has *numbered, sequential, testable steps*
- [ ] Format specifies *exact output structure*
- [ ] Audience defines *reading level* and *vocabulary*

### CRAFT Variants
| Variant | Use Case |
|---------|----------|
| **CRAFT** | General purpose, high quality |
| **CRAFT+CoT** | Add Chain-of-Thought to Action steps |
| **CRAFT-FewShot** | Include examples in Context |
| **CRAFT-Code** | Format=code, Role=senior engineer |
| **CRAFT-Analytical** | Role=analyst, Format=structured report |

### References
- [Original Video](https://youtu.be/3fVAtaGhUyU) — Dreams of Code
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library)