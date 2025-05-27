from dotenv import load_dotenv
import requests
import os

load_dotenv()  # Loads variables from .env

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def query_openrouter(prompt, model="openai/gpt-3.5-turbo"):
    if not OPENROUTER_API_KEY:
        raise ValueError("Missing OpenRouter API Key. Please set OPENROUTER_API_KEY env variable.")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a solar energy expert. Given rooftop details, respond with structured solar panel installation advice."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise RuntimeError(f"API call failed: {response.status_code}, {response.text}")
