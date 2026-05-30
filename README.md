# LLM Playground

A local command-line interface for testing and interacting with multiple Large Language Models (LLMs) from various providers.

## Overview

This project provides a unified command-line interface to test different LLM providers including Cerebras, Cloudflare, Z.ai, Gemini, Groq, and more. It allows developers to quickly configure API keys and test prompts against multiple models without switching between different tools.

## Features

- **Multi-provider Support**: Access to 13 different LLM providers
- **Environment Variable Management**: Easy configuration through `.env` file
- **Interactive CLI**: Simple menu-driven interface for selecting providers and actions
- **Usage Checking**: Option to check usage information with various services
- **Local Development Focus**: Designed for testing and development purposes only

## Supported Providers

| Provider        | Environment Variables |
|----------------|----------------------|
| Cerebras       | `CEREBRAS_API_KEY` |
| Cloudflare     | `CLOUDFLARE_API_KEY`, `CLOUDFLARE_ACCOUNT_ID` |
| Z.ai           | `ZAI_API_KEY` |
| Gemini         | `GEMINI_API_KEY` |
| AgentRouter    | `AGENTROUTER_API_KEY` |
| Ollama         | `OLLAMA_API_KEY` |
| And 8 more     | (See playground.py for complete list) |

## Installation

1. Clone this repository
2. Install required Python packages:
   ```bash
   pip install python-dotenv requests
   ```
3. Create your `.env` file based on the sample:
   ```bash
   cp .env.sample .env
   ```

## Usage

Run the playground:
```bash
python playground.py
```

You'll be presented with a menu of available providers. Select a provider number (1-13) and then choose:
- **1. Prompt**: Enter a prompt to send to the selected LLM
- **2. Check usage**: Get usage information for the current provider

## Configuration

1. Create a `.env` file by copying `.env.sample`
2. Add your API keys for the providers you want to use
3. The script will automatically load these environment variables

## Security Notes

- Never commit your `.env` file to version control
- This skill is intended for local development only
- API keys are stored in the `.env` file and managed by the application
- Keys are masked in confirmations for security

## Environment Variables

The `.env` file should contain your API keys in the following format:
```
CEREBRAS_API_KEY=your_cerebras_key_here
CLOUDFLARE_API_KEY=your_cloudflare_key_here
CLOUDFLARE_ACCOUNT_ID=your_account_id_here
ZAI_API_KEY=your_zai_key_here
GEMINI_API_KEY=your_gemini_key_here
AGENTROUTER_API_KEY=your_agentrouter_key_here
OLLAMA_API_KEY=your_ollama_key_here
```

## License

This project is designed for personal use and testing purposes only.