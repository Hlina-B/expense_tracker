from expense_tracker.models.expnse_mc import Expense
from expense_tracker.db.data_layer.db_helper import get_path
from datetime import datetime
from pathlib import Path
import json
import csv
import os
import sys

file_name: str = "expense.json"

def read_file() -> dict[int, Expense]:
    path = get_path(file_name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return {v["id"]:to_expense(v) for v in data.values()}
    return {}

def write_file(data: dict[int, Expense]):
    path = get_path(file_name)
    with open(path, "w", encoding="utf-8") as file:
        json.dump({v.id:to_dict(v) for v in data.values()}, file, indent=4, ensure_ascii=False)

def export_to_csv(args):
    if not (args.path.exists() and args.path.is_dir()):
        print("Path must exist and must be a directory.")
        sys.exit(-1)
        
    data = read_file()
    if len(data) == 0:
        print("There is no expense to export to csv.")
        return
    
    to_cvs_dict = [to_dict(v) for v in data.values()]
    headers = to_cvs_dict[0].keys()
    path = args.path / "expenses.csv"
    with open(path, "w", newline="", encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(to_cvs_dict)

def to_expense(v: dict) -> Expense:
    id = v['id']
    description = v['description']
    category = v['category']
    createdAt = datetime.strptime(v['createdAt'], "%Y-%m-%d %H:%M:%S")
    updatedAt = datetime.strptime(v['updatedAt'], "%Y-%m-%d %H:%M:%S") if v['updatedAt'] is not None else None
    amount = v['amount']
    return Expense(id, description, category, createdAt, updatedAt, amount)

def to_dict(v: Expense)-> dict:
    return {
        "id": v.id,
        "description": v.description, 
        "category": v.category, 
        "createdAt": v.createdAt.strftime("%Y-%m-%d %H:%M:%S"), 
        "updatedAt": v.updatedAt.strftime("%Y-%m-%d %H:%M:%S") if v.updatedAt is not None else None, 
        "amount": v.amount
    }