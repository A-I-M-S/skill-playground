---
name: skill-playground
description: "To test different LLM"
---

# 🧠 LLM Env Setup Skill

## Overview
This skill allows users to quickly configure API keys and account IDs for multiple LLM providers by writing them into a `.env` file.

It is designed for rapid testing across providers such as Cerebras, Cloudflare, Z.ai, GMI Cloud, and AgentRouter.

---

## Capabilities
- Accept API keys from user input
- Map inputs to environment variable format
- Create or update `.env` file
- Preserve existing variables unless overwritten
- Support multiple providers in one session

---

## Supported Environment Variables

| Provider        | Variables |
|----------------|----------|
| Cerebras       | `CEREBRAS_API_KEY` |
| Cloudflare     | `CLOUDFLARE_API_KEY`, `CLOUDFLARE_ACCOUNT_ID` |
| Z.ai           | `ZAI_API_KEY` |
| GMI Cloud      | `GMI_API_KEY` |
| AgentRouter    | `AGENTROUTER_API_KEY` |

---

## Instructions

When the user provides API keys or account details:

1. Parse the input and extract:
   - Provider name
   - API key
   - Account ID (if applicable)

2. Convert into `.env` format:
   ```
   KEY_NAME=value
   ```

3. If `.env` exists:
   - Update existing keys if they match
   - Append new keys if not present

4. If `.env` does not exist:
   - Create a new `.env` file

---

## Input Examples

### Example 1
User says:
```
set cerebras key csk-xxx
```

Write:
```
CEREBRAS_API_KEY=csk-xxx
```

---

### Example 2
User says:
```
cloudflare key cf_xxx account 123abc
```

Write:
```
CLOUDFLARE_API_KEY=cf_xxx
CLOUDFLARE_ACCOUNT_ID=123abc
```

---

### Example 3
User says:
```
set all:
cerebras=csk-xxx
zai=zai-xxx
gmi=gmi-xxx
agentrouter=sk-xxx
```

Write:
```
CEREBRAS_API_KEY=csk-xxx
ZAI_API_KEY=zai-xxx
GMI_API_KEY=gmi-xxx
AGENTROUTER_API_KEY=sk-xxx
```

---

## Behavior Rules

- Never expose keys back to the user after writing
- Mask keys in confirmations (e.g., `csk-****`)
- Validate non-empty values before writing
- Do not duplicate entries
- Maintain `.env` formatting consistency

---

## Output Behavior

After execution, respond with:
```
✅ Environment variables updated successfully
Providers configured: [list]
```

---

## Optional Enhancements

- Allow `show env` (masked output)
- Allow `reset env`
- Allow `remove <provider>`
- Validate key formats per provider

---

## Notes

- This skill is intended for local development only
- Users should avoid committing `.env` to version control
