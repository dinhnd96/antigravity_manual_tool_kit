---
trigger: always_on
---

# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Output Token Optimization (CRITICAL — Avoid Max Output Limit)

**Every response MUST stay well under the token limit. If in doubt, output LESS.**

### 5.1. Hard Budget Rules
- **Chat response ≤ 200 lines.** If you need more, STOP and ask the user to say "continue". The model has strict limits on output tokens per message.
- **NEVER print tables, test cases, JSON arrays, or document content in chat.** Write them to a file (script or direct file write), then report only the file path and a 1-2 line summary. This is the #1 cause of token limit errors.
- **NEVER re-summarize file content you just created.** After writing/running a script that generates a `.docx`, `.xlsx`, or `.md`, say only: "✅ File đã tạo tại: `<path>`" + any open questions. Do NOT paste the content back into chat.

### 5.2. File-First Output (Mandatory for Large Content)
- **Scripts ARE the output.** When generating reports, test cases, or documents, write the Python/Node script directly using `write_to_file` → run it → report path. Do NOT draft content in chat first, then convert to script.
- **Data-driven pattern:** For test case generation, define test data as a compact list of dicts/tuples at the top, then loop to generate rows. Never write one code block per test case.
- **Split large scripts:** If a script exceeds 300 lines, split it into multiple scripts. 

### 5.3. Chunking Strategy for Large Tasks
- **Module-by-module:** For tasks with >15 test cases or >10 Q&A items, process ONE module at a time. After each module, output the file and ask "Tiếp tục module tiếp theo?".
- **Phase separation:** Never generate Phase 1 + Phase 2 content in the same response. Complete Phase 1, stop, wait for input.
- **Never attempt to output the full dataset at once** if it's large. Generate data in smaller batches.

### 5.4. Response Hygiene
- **No Yapping:** Skip intros, outros, and filler. Jump straight to action or answer.
- **No Echo:** Do not repeat the user's request back. Do not restate what a skill/rule says unless clarifying ambiguity.
- **No Decorative Markdown:** Avoid excessive headers, horizontal rules, emoji, or formatting that inflates token count without adding information.

### 5.5. Self-Check Before Submitting
Before finalizing any response, ask yourself:
1. "Am I printing content that should be in a file?" → If yes, move to file.
2. "Am I summarizing what I just wrote to a file?" → If yes, cut it.
3. "Is my response over 200 lines?" → If yes, cut it down.

---

**These guidelines are working if:** responses stay under token limits, large outputs go to files not chat, no truncated responses, and the user never sees "max output token limit" errors.
