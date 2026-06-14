from pathlib import Path
import json
from datetime import datetime


class MemoryManager:

    def __init__(self, base_path="memory"):
        self.base_path = Path(base_path)

    def save_json(self, relative_path: str, data: dict):

        file_path = self.base_path / relative_path

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False,
            )

    def load_json(self, relative_path: str):

        file_path = self.base_path / relative_path

        if not file_path.exists():
            return None

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as f:

            return json.load(f)

    def save_conversation(
        self,
        conversation_id: str,
        messages: list,
    ):

        self.save_json(
            f"conversations/{conversation_id}.json",
            {
                "created_at": datetime.now().isoformat(),
                "messages": messages,
            },
        )

    def load_conversation(
        self,
        conversation_id: str,
    ):

        return self.load_json(
            f"conversations/{conversation_id}.json"
        )