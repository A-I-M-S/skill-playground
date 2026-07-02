from dotenv import load_dotenv
import requests,time,os
load_dotenv()

PROVIDERS = {
    "1": {"name": "Cerebras", "model": "z-ai/glm-4.7", "pro": "Cerebras"},
    "2": {"name": "Cloudflare", "model": "z-ai/glm-4.7-flash", "pro": "cloudflare"},
    "3": {"name": "Z.ai", "model": "z-ai/glm-5.1", "pro": "Z.ai"},
    "4": {"name": "Moonshot", "model": "moonshotai/kimi-k2.6", "pro": "Moonshot AI"},
    "5": {"name": "Gemini", "model": "google/gemini-2.5-flash", "pro": "Google AI Studio"},
    "6": {"name": "Xiaomi", "model": "xiaomi/mimo-v2-flash", "pro": "Xiaomi"},
    "7": {"name": "MiniMax", "model": "minimax-m3", "pro": "minimax/highspeed"},
    "8": {"name": "Together AI", "model": "z-ai/glm-5.1", "pro": "Together"},
    "9": {"name": "Groq", "model": "openai/gpt-oss-120b", "pro": "groq"},
    "10": {"name": "AgentRouter", "model": "deepseek-v3.2", "url": "s://agentrouter.org/v1", "key": "AGENTROUTER_AK"},
    "11": {"name": "Ollama", "model": "gemma4:31b-cloud", "url": "s://ollama.com/v1", "key": "OLLAMA_AK"},
    "12": {"name": "Ollama CN", "model": "llama-ac", "url": "://ollama.insightginie.com/v1", "key": "OLLAMA_CN"},
    "13": {"name": "NS2E", "model": "openai/gpt-5.5", "url": "://ca.ns2e.com/v1", "key": "NS2E_AK"},
    "14": {"name": "Bedrock", "model": "anthropic/claude-opus-4.6", "pro": "amazon-bedrock/us-east-1"},
    "15": {"name": "OpenAI", "model": "openai/gpt-5.5-pro", "pro": "openai"},
    "16": {"name": "Dough", "model": "kr/deepseek-3.2-thinking-agentic", "url": "s://dough.id/api/v1", "key": "DOUGH_AK"},
    "17": {"name": "Byteplus", "model": "seed-2-0-pro-260328", "url": "s://ark.ap-southeast.bytepluses.com/api/v3", "key": "BYTEPLUS_AK"},
    "18": {"name": "HuggingFace", "model": "zai-org/GLM-5.2", "url": "s://router.huggingface.co/v1", "key": "HF_AK"},
    "19": {"name": "NVIDIA", "model": "nvidia/nemotron-3-ultra-550b-a55b", "url": "s://integrate.api.nvidia.com/v1", "key": "NVIDIA_AK"},
    "20": {"name": "Tencent", "model": "hy-mt2-plus", "url": "s://tokenhub-intl.tencentcloudmaas.com/v1", "key": "TENCENT_AK"},
    "21": {"name": "Alibaba", "model": "qwen3.7-plus", "url": "s://ws-iyhoobdzibk5p0wv.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", "key": "ALI_AK"},
    "22": {"name": "Z.ai(coding)", "model": "glm-5.2", "url": "s://api.z.ai/api/coding/paas/v4", "key": "ZAICODING"}
}

def chat(pmt, mod, url=None, key=None, pro=None):
    start = time.time()
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions" if pro else f"http{url}/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv(key or 'OPENROUTER_AK')}",
            "Content-Type": "application/json"
        },
        json={
            "model": mod,
            "messages": [{"role": "user", "content": pmt}],
            **({"provider": {"order": [pro], "allow_fallbacks": False}} if pro else {"stream": False})
        }
    )
    print(f"\n⏱ Latency: {(time.time()-start):.2f}s")
    try: print(response.json()["choices"][0]["message"]["content"])
    except: print(response.text)

def check_usage(url=None, key=None, pro=None):
    if pro or not url:
        print("No usage found")
        return
    api_key = os.getenv(key or "OPENROUTER_AK")
    if not api_key:
        print("No usage found")
        return
    usage_url = f"http{url}/v1/usage"
    try:
        response = requests.get(
            usage_url,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            timeout=30,
        )
        data = response.json()
    except Exception:
        print("No usage found")
        return
    if response.status_code >= 400:
        print("No usage found")
        return
    print("\nUsage:")
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"- {k}: {v}")
    else:
        print(data)

if __name__=="__main__":
    while True:
        try:
            print("\n" + " | ".join(f"{k}. {v['name']}" for k, v in PROVIDERS.items()))
            c=input("\nSelect provider: ").strip()
        except: break
        provider = PROVIDERS.get(c)
        if not provider:
            break
        try:
            action = input("\n1. Prompt | 2. Check usage\nSelect action: ").strip()
        except:
            break
        if action == "1":
            try:
                p = input("\nEnter your prompt:\n> ")
            except:
                break
            chat(p, provider["model"], url=provider.get("url"), key=provider.get("key"), pro=provider.get("pro"))
        elif action == "2":
            check_usage(url=provider.get("url"), key=provider.get("key"), pro=provider.get("pro"))
        else:
            continue
