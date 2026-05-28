from expense_tracker.models.expnse_mc import Commands, SubCommands
from pathlib import Path
import argparse

def get_user_input(): 
    paraser = argparse.ArgumentParser(description="Expense Tracker App Arguments")
    commands = paraser.add_subparsers(dest="command", help="Available commands add, update, list, delete, summary, and export")
    add = commands.add_parser(Commands.ADD.value, help="Add a new expense Description of expense is mandatory. See help for all the add parameters.")
    update = commands.add_parser(Commands.UPDATE.value, help="Update expense. Id is required. You can update description, category, amount, and budget")
    delete = commands.add_parser(Commands.DELETE.value, help="Delete expense. Id is required")
    list_cmd = commands.add_parser(Commands.LIST.value, help="List expenses. You can filter by day or month of the current year.")
    summary = commands.add_parser(Commands.SUMMARY.value, help="Summary of expenses. You can filter by day or month of the current year")
    export = commands.add_parser(Commands.EXPORT.value, help="Export expesens to CSV.")
    
    add.add_argument(SubCommands.DESCRIPTION.value, required=True, type=str, help="Expense Description.")
    add.add_argument(SubCommands.AMOUNT.value, type=float, required=False, help="Expense Amount. Default value is 0.0")
    add.add_argument(SubCommands.CATEGORY.value, type=str, required=False, help="Add a category of expense")
    add.add_argument(SubCommands.BUDGET.value, type=float, required=False, help="Budget for the current month")

    update.add_argument(SubCommands.ID.value, required=True, type=int, help="Id is required to update.")
    update.add_argument(SubCommands.DESCRIPTION.value, type=str,  required=False, help="Update expense description.")
    update.add_argument(SubCommands.AMOUNT.value, type=float, required=False, help="Update expense of amount.")
    update.add_argument(SubCommands.CATEGORY.value, type=str, required=False, help="Update category of the expense")
    update.add_argument(SubCommands.BUDGET.value, type=float, required=False, help="Update budget")

    delete.add_argument(SubCommands.ID.value, required=True, type=int, help="ID is required to delete")

    list_cmd.add_argument(SubCommands.DAY.value, type=int, required=False, help="You can filter list by day")
    list_cmd.add_argument(SubCommands.MONTH.value, type=int, required=False, help="You can filter list by month")

    summary.add_argument(SubCommands.DAY.value, type=int, required=False,  help="You can filter summary by day")
    summary.add_argument(SubCommands.MONTH.value, type=int, required=False, help="You can filter summary by month.")
    
    export.add_argument(SubCommands.PATH.value, required=True, type=Path, help="Path is required.")

    return paraser.parse_args()
