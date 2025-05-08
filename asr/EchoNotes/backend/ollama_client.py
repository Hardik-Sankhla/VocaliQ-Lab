# backend/ollama_client.py
import requests

def call_ollama(prompt: str, model: str = "llama2") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=120
    )
    return response.json().get("response", "").strip()
