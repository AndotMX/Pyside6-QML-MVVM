import json
from socket import gethostname
from typing import Any

from .logger import log
from .path_helper import get_project_root


def load_cfg() -> dict[str, Any]:
    """
    Dynamically imports a env module based on the host name.

    If not found, imports mock.

    Returns:
        module: The imported configuration module.
    """
    cfg_dir = get_project_root() / "env_cfg"
    env_path = cfg_dir / gethostname() / ".json"

    if not env_path.is_file():
        log.warning(f"Could not import env configuration from env: '{gethostname()}'")
        log.warning("Importing mock")
        env_path = cfg_dir / "mock.json"

    with open(env_path, encoding="utf-8") as file:
        return json.load(file)
