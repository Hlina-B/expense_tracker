from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import sys

@dataclass
class Expense:
    id: int
    description: str
    category: str
    createdAt: datetime
    updatedAt: datetime
    amount: float = field(default=0.0)

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be less than zero.")
        
@dataclass
class Budget:
    id: str
    month: int
    year: int
    amount: float = field(default=0.0)
    
    def __post_init__(self):
        if not (isinstance(self.month, int) and (self.month >= 1 and self.month <=12)):
            print("Please provide the numberic value of the month and that cannot be less than 1 or greater than 12.")
            sys.exit(-1)
        current_year = datetime.now().year
        if not (isinstance(self.year, int) and (self.year == current_year)):
            print("You can only set a budget for current year and year must be numeric.")
            sys.exit(-1)


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
    DAY = "--day"
    MONTH = "--month"
    PATH = "--path"

class BCommands(Enum):
    BADD = "badd"
    BUPDATE = "bupdate"
    BLIST = "blist"
    BDELETE = "bdelete"

class BSubCommands(Enum):
    BMONTH = "--bmonth"
    BAMOUNT = "--bamount"
