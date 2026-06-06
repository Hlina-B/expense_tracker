from expense_tracker.models.expnse_mc import Budget, BCommands, Expense
from expense_tracker.db.data_layer.budget_tracker_data import read_budget_file, write_budget_file
from expense_tracker.service.helper import build_budget_id
from datetime import datetime
import sys

current_year = datetime.now().year

def b_dispatcher(args):
    match args.command:
        case BCommands.BADD.value:
            add(args)
        case BCommands.BUPDATE.value:
            update(args)
        case BCommands.BDELETE.value:
            delete(args)
        case BCommands.BLIST.value:
            list_budget()
        case _:
            print("Unknown Budget Command. Good Bye.")

def add(args):
    budgets = read_budget_file()
    id = build_budget_id(args.bmonth)
    budget = budgets.get(id)
    if budget is not None:
        print(f"There is already a budget for {budget.month}. You can update the amount but you cannot more than one buget for a single month")
        return
    budget = Budget(id, args.bmonth, current_year, args.bamount)
    budgets.setdefault(id, budget)
    write_budget_file(budgets)
    print("Budget addd successfully.")

def update(args):
    id = build_budget_id(args.bmonth)
    budgets = read_budget_file()
    budget = budgets.get(id)
    if budget is None:
        print("There is no budget for the given month.")
        return
    budget.amount = args.bamount
    write_budget_file(budgets)
    print("Updated Successfully.")

def delete(args):
    id = build_budget_id(args.bmonth)
    budgets = read_budget_file()
    budget = budgets.pop(id, None)
    if budget is None:
        print("There is no budget for the given month")
        return
    write_budget_file(budgets)
    print("Deleted Successfully.")

def list_budget():
    budgets = read_budget_file()
    if len(budgets) == 0:
        print("There is no budget to list.")
        return
    
    print(f"\n{'ID':<10}  |  {'Month':<5}  |  {'Year':<5}  |  {'Amount':<10}")
    print("-" * 45)
    for budget in budgets.values():
        print(f"{budget.id:<10}  |  {budget.month:<5}  |  {budget.year:<5}  |  {budget.amount:<10}")

def check_available_budget(expenses: dict[int, Expense], month: int):
    total_outlays = sum(exp.amount for exp in expenses.values() if exp.createdAt.month == month)
    budget_record = read_budget_file().get(build_budget_id(month))

    return (budget_record.amount - total_outlays) if budget_record else None
