from expense_tracker.models.expnse_mc import Expense
from datetime import datetime
from collections.abc import Iterable

def any_one_attribute(args) -> bool:
    params = [args.description, args.category, args.amount]
    if any(params):
        return True
    
    return False

def buildExpenseObject(id: int, args) -> Expense:
    return Expense(
        id = id,
        description = args.description,
        category = args.category,
        createdAt = datetime.now(),
        updatedAt = None,
        amount = args.amount if args.amount is not None else 0.0
    )

def updateExpenseObject(args, expense: Expense) -> Expense:
    expense.updatedAt = datetime.now()
    expense.amount = args.amount if args.amount is not None and args.amount >= 0 else expense.amount
    expense.category = args.category if args.category is not None else expense.category
    expense.description = args.description if args.description is not None else expense.description
    return expense

def budget_evaluation():
    # To Do: This requires a different logic than individual expenses. To be implemented.
    pass

def fliter_by_dm(args, data: dict[int, Expense]) -> Iterable:
    if args.day is not None and args.month is not None:
        return list(filter(lambda x: x.createdAt.day == args.day and x.createdAt.month == args.month, data.values()))
    elif args.month is not None:
        return list(filter(lambda x: x.createdAt.month == args.month, data.values()))
    elif args.day is not None:
        return list(filter(lambda x: x.createdAt.day == args.day, data.values()))
    else:
        return data.values()

def build_budget_id(month: int):
    current_year = datetime.now().year
    return str(month) + "-" + str(current_year)

def budget_status(budget: float):
    if budget is None:
        print("\nThere is no budget set for this expense")
    elif budget < 0:
        print(f"\nYou over your budget by {budget}") 
    else:
        print(f"\nYou are left with {budget}")