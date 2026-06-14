import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5-coder:7b",
    "prompt": "Responde únicamente: Hola TripleA",
    "stream": False,
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())