import requests
from typing import List, Dict, Any


class OllamaClient:

    def __init__(self, host: str = "http://localhost:11434"):
        self.host = host.rstrip("/")

    def health(self) -> bool:
        try:
            response = requests.get(
                f"{self.host}/api/tags",
                timeout=5
            )

            return response.status_code == 200

        except Exception:
            return False

    def list_models(self) -> List[Dict[str, Any]]:

        response = requests.get(
            f"{self.host}/api/tags"
        )

        response.raise_for_status()

        data = response.json()

        return data.get("models", [])

    def generate(
        self,
        model: str,
        prompt: str,
        stream: bool = False,
    ):

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": stream,
            },
        )

        response.raise_for_status()

        return response.json()

    def chat(
        self,
        model: str,
        messages: list,
        stream: bool = False,
    ):

        response = requests.post(
            f"{self.host}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": stream,
            },
        )

        response.raise_for_status()

        return response.json()