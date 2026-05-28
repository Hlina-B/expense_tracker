from expense_tracker.models.expnse_mc import Expense
from datetime import datetime
from collections.abc import Iterable

def any_one_attribute(args) -> bool:
    params = [args.description, args.category, args.budget, args.amount]
    if any(params):
        return True
    
    return False

def buildExpenseObject(id: int, args) -> Expense:
    return Expense(
        id = id,
        description = args.description,
        category = args.category,
        budget = args.budget,
        createdAt = datetime.now(),
        updatedAt = None,
        amount = args.amount if args.amount is not None else 0.0
    )

def updateExpenseObject(args, expense: Expense) -> Expense:
    expense.updatedAt = datetime.now()
    expense.amount = args.amount if args.amount is not None and args.amount >= 0 else expense.amount
    expense.category = args.category if args.category is not None else expense.category
    expense.budget = args.budget if args.budget is not None and args.budget >= 0 else expense.budget
    expense.description = args.description if args.description is not None else expense.description
    return expense

def fliter_by_dm(args, data: dict[int, Expense]) -> Iterable:
    if args.day is not None and args.month is not None:
        return list(filter(lambda x: x.createdAt.day == args.day and x.createdAt.month == args.month, data.values()))
    elif args.month is not None:
        return list(filter(lambda x: x.createdAt.month == args.month, data.values()))
    elif args.day is not None:
        return list(filter(lambda x: x.createdAt.day == args.day, data.values()))
    else:
        return data.values()
    
 

