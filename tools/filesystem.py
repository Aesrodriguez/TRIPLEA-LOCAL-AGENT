from pathlib import Path
from typing import List


class FileSystemTool:
    """Herramientas para interactuar con el sistema de archivos."""

    @staticmethod
    def list_directory(path: str = ".") -> List[str]:
        p = Path(path)

        if not p.exists():
            return []

        return sorted([item.name for item in p.iterdir()])

    @staticmethod
    def create_directory(path: str) -> bool:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True

    @staticmethod
    def create_file(path: str) -> bool:
        Path(path).touch(exist_ok=True)
        return True

    @staticmethod
    def read_file(path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    @staticmethod
    def write_file(path: str, content: str) -> bool:
        Path(path).write_text(content, encoding="utf-8")
        return True

    @staticmethod
    def exists(path: str) -> bool:
        return Path(path).exists()

    @staticmethod
    def find_files(path=".", pattern="*"):
        return [str(p) for p in Path(path).rglob(pattern)]