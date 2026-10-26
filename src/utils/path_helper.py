from pathlib import Path


def get_project_root() -> Path:
    """Finds the root directory of the project by searching for the 'pyproject.toml' file in the parent directories.

    Returns:
        Path: Project directory path.
    """
    return next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())


def get_source_root() -> Path:
    """Finds the source root directory of the project by searching for the 'src' folder in the parent directories.

    Returns:
        Path: Source root directory path.
    """
    return get_project_root() / "src"
