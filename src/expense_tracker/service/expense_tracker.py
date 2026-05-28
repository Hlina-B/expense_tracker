from expense_tracker.models.expnse_mc import Commands
from expense_tracker.db.data_layer.expense_tracker_data import read_file, write_file, export_to_csv
from expense_tracker.service.helper import buildExpenseObject, updateExpenseObject, any_one_attribute, fliter_by_dm
import sys

def dispatcher(args):
    if args.command is None:
        print("Unknow command. Check 'expense -h' for available commands. Good bye.")
        sys.exit(-1)

    match args.command:
        case Commands.ADD.value:
            add(args)
        case Commands.UPDATE.value:
            update(args)
        case Commands.DELETE.value:
            delete(args)
        case Commands.LIST.value:
            list_expense(args)
        case Commands.SUMMARY.value:
            summary(args)
        case Commands.EXPORT.value:
            export(args) 
        case _:
            print("Unknow command. Check 'expense -h' for available commands. Good bye.")

def add(args):
    data = read_file()
    id = max(data.keys(), default=0) + 1
    expense = buildExpenseObject(id, args)
    data.setdefault(id, expense)
    write_file(data)
    print("Expense added sucessfuly.")   

def update(args):
    if not any_one_attribute(args):
        print("You have to provide at least one update value.")
        sys.exit(-1)
    
    data = read_file()
    expense = data.get(args.id)
    if expense is None:
        print("Item not Found. Please be sure the ID is correct.")
        return

    updateExpenseObject(args, expense)
    write_file(data)
    print("Expense Updated Sucessfully.")

def delete(args):
    data = read_file()
    expense = data.pop(args.id, None)

    if expense is None:
        print("Deleted sucessful. The ID provided is not found.")
        return 
    write_file(data)
    print("Deleted Sucessfully.")

def list_expense(args):
    expenses = read_file()
    data = fliter_by_dm(args, expenses)
    if len(data) == 0:
        print("There is no expense data to show")
        return

    print(f'\n{"ID":<5}  |  {"Date":<12}  |  {"Description":<20}  |  {"Amount":<12}  |  {"Category":<12}  |  {"Budget":<12}')
    print("-" * 95)
    for expense in data:
        category = expense.category if expense.category is not None else "N/A" # This can be improved if you don't like defensive approach. 
        budget = expense.budget if expense.budget is not None else "N/A" # same as the above 
        date = expense.createdAt.date().strftime("%Y-%m-%d")
        print(f'{expense.id:<5}  |  {date:<12}  |  {expense.description:<20}  |  {expense.amount:<12}  |  {category:<12}  |  {budget:<12}')


def summary(args):
    expenses = read_file()
    data = fliter_by_dm(args, expenses)
    total = 0
    for expense in data:
        total += expense.amount
    
    print(f"Total expenses: ${total}")

def export(args):
    export_to_csv(args)
    print("Exported Sucessfully")


