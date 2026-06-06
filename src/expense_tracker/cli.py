from expense_tracker.models.expnse_mc import Commands, SubCommands, BCommands, BSubCommands
from pathlib import Path
import argparse
import sys

def get_user_input():
    paraser = argparse.ArgumentParser(description="Expense Tracker App Arguments")
    commands = paraser.add_subparsers(dest="command", help="Use Appropriate command. Use 'expense -h' for help")
    get_expense_input(commands)
    get_budget_input(commands)

    args = paraser.parse_args()
    if args.command is None:
        print("Please use either 'exp' or 'budg' command after 'expense.")
        sys.exit(-1)
    
    return paraser.parse_args()


def get_expense_input(exp): 
    add = exp.add_parser(Commands.ADD.value, help="Add a new expense Description of expense is mandatory. See help for all the add parameters.")
    update = exp.add_parser(Commands.UPDATE.value, help="Update expense. Id is required. You can update description, category, and amount")
    delete = exp.add_parser(Commands.DELETE.value, help="Delete expense. Id is required")
    list_cmd = exp.add_parser(Commands.LIST.value, help="List expenses. You can filter by day or month of the current year.")
    summary = exp.add_parser(Commands.SUMMARY.value, help="Summary of expenses. You can filter by day or month of the current year")
    export = exp.add_parser(Commands.EXPORT.value, help="Export expesens to CSV.")
    
    add.add_argument(SubCommands.DESCRIPTION.value, required=True, type=str, help="Expense Description.")
    add.add_argument(SubCommands.AMOUNT.value, type=float, required=False, help="Expense Amount. Default value is 0.0")
    add.add_argument(SubCommands.CATEGORY.value, type=str, required=False, help="Add a category of expense")

    update.add_argument(SubCommands.ID.value, required=True, type=int, help="Id is required to update.")
    update.add_argument(SubCommands.DESCRIPTION.value, type=str,  required=False, help="Update expense description.")
    update.add_argument(SubCommands.AMOUNT.value, type=float, required=False, help="Update expense of amount.")
    update.add_argument(SubCommands.CATEGORY.value, type=str, required=False, help="Update category of the expense")

    delete.add_argument(SubCommands.ID.value, required=True, type=int, help="ID is required to delete")

    list_cmd.add_argument(SubCommands.DAY.value, type=int, required=False, help="You can filter list by day")
    list_cmd.add_argument(SubCommands.MONTH.value, type=int, required=False, help="You can filter list by month")

    summary.add_argument(SubCommands.DAY.value, type=int, required=False,  help="You can filter summary by day")
    summary.add_argument(SubCommands.MONTH.value, type=int, required=False, help="You can filter summary by month.")
    
    export.add_argument(SubCommands.PATH.value, required=True, type=Path, help="Path is required.")



def get_budget_input(budg):
    add = budg.add_parser(BCommands.BADD.value, help="Month is required")
    update = budg.add_parser(BCommands.BUPDATE.value, help="Amount is required")
    delete = budg.add_parser(BCommands.BDELETE.value, help="Month is required")
    budg.add_parser(BCommands.BLIST.value, help="List all budgets allocated for the current yea")

    add.add_argument(BSubCommands.BMONTH.value, type=int, required=True, help="The month for the Budget")
    add.add_argument(BSubCommands.BAMOUNT.value, type=float, required=False, help="The amount of budget for the month")

    update.add_argument(BSubCommands.BMONTH.value, type=int, required=True, help="Month is required")
    update.add_argument(BSubCommands.BAMOUNT.value, type=float, required=True, help="Amount is the only field that can be updated and it is required")
    
    delete.add_argument(BSubCommands.BMONTH.value, type=int, required=True, help="Month is required")

    
