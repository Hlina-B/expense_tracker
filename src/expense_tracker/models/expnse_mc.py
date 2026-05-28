from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

@dataclass
class Expense:
    id: int
    description: str
    category: str
    budget: float # This is predetermined to be a monthly budget.
    createdAt: datetime
    updatedAt: datetime
    amount: float = field(default=0.0)

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be less than zero.")
        if isinstance(self.budget, int) and self.budget < 0:
            raise ValueError("Budget Cannot be less than zero")

class Commands(Enum):
    ADD = "add"
    UPDATE = "update"
    LIST = "list"
    DELETE = "delete"
    SUMMARY = "summary"
    EXPORT = "export"

class SubCommands(Enum):
    ID = "--id"
    DESCRIPTION = "--description"
    CATEGORY = "--category"
    AMOUNT = "--amount"
    BUDGET = "--budget"
    DAY = "--day"
    MONTH = "--month"
    PATH = "--path"
