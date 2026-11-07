LOG: [LEARN] Reference: PromptMaxer — Prompt Expansion Framework

**Title:** PromptMaxer
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** PromptMaxer.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Activation
Trigger on: "prompt" + "max"/"maxer"/"maxing"/"maximize" (and variations)

### Two Modes
| Mode | Trigger | Behavior |
|------|---------|----------|
| **Return Mode** | "PromptMaxer this", "expand this" | Return expanded prompt to user |
| **Execute Mode** | "Use PromptMaxer for", "Apply and do" | Use internally, deliver final output |

**Default:** Return Mode if ambiguous

### Four-Stage Pipeline (Every Activation)

#### Stage 1: Deconstruct
Extract intent — Action, Subject, Format, Audience, Purpose, Domain, Constraints

#### Stage 2: Diagnose
Identify gaps — Audience, Format, Scope, Tone, Purpose, Success Criteria, Constraints, Context
Classify: Minimal / Moderate / Severe gaps

#### Stage 3: Develop (10 Techniques)
1. **Role Assignment** — Expert identity with credibility
2. **Context Layering** — Audience, situational, domain, constraint context
3. **Output Specification** — Exact format, length, structure, style
4. **Task Decomposition** — Break into sequential steps
5. **Chain-of-Thought** — Explicit reasoning for complex tasks
6. **Few-Shot Framing** — Pattern/examples to follow
7. **Constraint Definition** — Must include/avoid/maintain/exclude
8. **Clarity & Specificity** — Replace vague with concrete
9. **Success Criteria** — Observable quality indicators
10. **Meta-Guidance** — Ambiguity handling, assumptions, self-correction

**Task-Type Technique Matching:**
| Task | Primary | Secondary |
|------|---------|-----------|
| Creative | Role + Context + Output Spec + Constraints | Success Criteria |
| Technical | Role + Decomposition + CoT + Constraints | Output Spec |
| Educational | Role + Context + Output Spec | Decomposition + Success Criteria |
| Analytical | Role + CoT + Success Criteria | Context + Output Spec |
| Strategic | Role + Context + CoT + Constraints | Success Criteria |
| Communication | Role + Context + Output Spec + Constraints | Success Criteria |
| Code | Role + Decomposition + Constraints + Output Spec | CoT |

#### Stage 4: Deliver
**Structure:**
```
## ROLE
[Expert identity with credibility]

## CONTEXT
[Audience, situation, domain, constraints]

## TASK
[Clear, specific objective]

## REQUIREMENTS
- Format: [Structure]
- Length: [Bounds]
- Style: [Tone/voice]
- Include: [Required]
- Avoid: [Prohibited]

## APPROACH
[Methodology/steps]

## SUCCESS CRITERIA
[Observable quality indicators]
```

### Output Protocol

**Return Mode:** Output full expanded prompt, formatted, copyable
**Execute Mode:** Use internally, deliver final output (don't show prompt)

## The "Blueprint" (The Why/Logic)

### Core Principle
Raw prompt = raw material. Expanded prompt = refined output. Gap = expertise human lacks time for.

**Return Mode:** User gets refined prompt to deploy anywhere.
**Execute Mode:** AI uses refined prompt on itself — becomes both prompt engineer and executor.

### Why 4 Stages?
1. **Deconstruct** — Isolate true intent from noise
2. **Diagnose** — Find what's missing before building
3. **Develop** — Apply proven techniques systematically
4. **Deliver** — Package for immediate use or execution

### Technique Selection Logic
- Task type determines primary techniques
- More relevant context = better output
- Specific beats general
- Usable now > perfect later

## The "Deep Dive" (The Technical Root)

### Pipeline as Prompt Injection (Execute Mode)
```
User Input → Deconstruct → Diagnose → Develop → Deliver
                ↓              ↓          ↓         ↓
           Intent Map    Gap Report  Technique Set  Final Prompt
                                                        ↓
                                              Execute with it
                                              → Final Output
```

### Continuous Mode
- Apply to all subsequent prompts
- Accumulate context
- Adapt techniques per task type
- Default Execute Mode (user wants results, not prompts)

### Operational Rules
| Always | Never |
|--------|-------|
| Determine mode first | Ask clarifying questions |
| Run full pipeline | Refuse to expand |
| Apply task-type techniques | Output vague expansions |
| Gather context intelligently | Require multiple rounds |
| Make reasonable assumptions | Add unnecessary preamble |

### Judgment Calls
- Relevant context improves; irrelevant clutters
- Specific > general
- Usable now > perfect later
- Default Return Mode if uncertain
- Default Execute Mode for continuous use

### References
- Chain-of-Thought (Wei et al., 2022)
- Few-Shot Prompting (Brown et al., 2020)
- Meta-Prompting (Wang et al., 2023)