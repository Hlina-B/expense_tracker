from expense_tracker.models.expnse_mc import Budget
from expense_tracker.db.data_layer.db_helper import get_path
from datetime import datetime
from dataclasses import asdict
from pathlib import Path
import json
import os

file_name: str = "budget.json"

def read_budget_file() -> dict[str, Budget]:
    path: Path = get_path(file_name)

    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r", encoding='utf-8') as file:
            data = json.load(file)
            return {v["id"]: Budget(**v) for v in data.values()}
        
    return {}

def write_budget_file(data: dict[str, Budget]):
    path: Path = get_path(file_name)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump({v.id: asdict(v) for v in data.values()}, file, indent=4, ensure_ascii=False)