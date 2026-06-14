from pathlib import Path
import yaml

CONFIG_PATH = Path("config/config.yaml")


def load_config():
    """Carga la configuración desde config.yaml"""

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"No existe el archivo: {CONFIG_PATH}"
        )

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)