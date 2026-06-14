from llm.ollama_client import OllamaClient

client = OllamaClient()

print("=" * 50)
print("HEALTH")
print("=" * 50)

print(client.health())

print()

print("=" * 50)
print("MODELOS")
print("=" * 50)

models = client.list_models()

for model in models:
    print(model["name"])

print()

print("=" * 50)
print("GENERATE")
print("=" * 50)

response = client.generate(
    model="qwen2.5-coder:7b",
    prompt="Responde únicamente: Hola TripleA",
)

print(response["response"])

print()

print("=" * 50)
print("CHAT")
print("=" * 50)

chat = client.chat(
    model="qwen2.5-coder:7b",
    messages=[
        {
            "role": "user",
            "content": "Di solamente: Hola desde Chat",
        }
    ],
)

print(chat["message"]["content"])