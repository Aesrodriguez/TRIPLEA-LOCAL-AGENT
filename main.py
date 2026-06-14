from core.settings import load_config
from tools.ollama_client import OllamaClient


def main():

    config = load_config()

    host = config["ollama"]["host"]

    model = config["model"]["default"]

    client = OllamaClient(host)

    print("=" * 50)
    print("TripleA Local Agent")
    print("=" * 50)

    if not client.health_check():
        print("❌ Ollama no está disponible")
        return

    print("✅ Ollama conectado\n")

    print("Modelos instalados:\n")

    models = client.list_models()

    for item in models:
        print("-", item["name"])

    print("\nEnviando prueba...\n")

    result = client.generate(
        model=model,
        prompt="Responde únicamente: Hola TripleA",
    )

    print(result["response"])


if __name__ == "__main__":
    main()