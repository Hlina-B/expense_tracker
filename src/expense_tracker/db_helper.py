from pathlib import Path

def get_path(file_name: str) -> Path:
    current_directory = Path(__file__).parent.parent
    file_path = current_directory / "storage" / file_name
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path