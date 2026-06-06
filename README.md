# Expense Tracker CLI

A lightweight, native Command Line Interface (CLI) application built in Python to track, manage, and audit daily expenses. It features monthly budgeting constraints, custom categorization, and structured data exporting.

## Project Architecture

The application implements a clean, decoupled 3-tier architecture:
* `UI/cli.py`: Front-end argument parser driven by the standard library's `argparse`.
* `service/expense_tracker.py`: Business logic orchestrator and dispatch controller.
* `db/data_layer/expense_tracker_data.py`: Serialization and file I/O operations engine.

## Installation

To install the application locally in "Editable" mode, navigate to the root directory (`expense_tracker/`) containing your `pyproject.toml` and run:

```bash
pip install -e .

Usage Examples
1. Add an Expense
The description is mandatory. Amount, category, and budget variables are optional.
expense add --description "Groceries" --amount 45.50 --category "Food" --budget 500.0

2. List Logged Expenses
View a formatted tabular matrix of all expenses, with optional date filters.
expense list
expense list --month 5 --day 28

3. Review Financial Summaries
Calculate total running costs globally or target a specific period.
expense summary
expense summary --month 5

4. Update or Delete Records
Modify specific fields or wipe records securely by unique Identifier tags.
expense update --id 1 --amount 52.00 --description "Weekly Groceries"
expense delete --id 1

5. Export Data
Dump the underlying JSON database into a clean, platform-agnostic CSV format.
expense export --path C:\\path\to\your\dir

## 6. Budgeting Management Sub-Commands (budg)

The application provides an absolute, monthly budgeting bounds matrix. When expenses are recorded or modified, the tracking engine cross-evaluates live outlays against your monthly metrics on-the-fly.

### Allocate a Monthly Budget Limit
Assign an investment limit for a specific numerical calendar month index (e.g., Month `8` for August).
```bash
expense badd --bmonth 8 --bamount 1200.00

Review Target Balances
List all current-year allocations in a formatted data table:
expense blist

Modify or Revoke Limits
Update allowances or remove a month's criteria securely:
expense bupdate --bmonth 8 --bamount 1500.00
expense bdelete --bmonth 8

On-the-Fly Enforcement Triggers
When adding or updating an expense, the interface automatically audits your allocation balances:
    - Under Allocation: You are left with 245.50
    - Exceeded Allocation: You over your budget by -15.20
    - Unconfigured Allocation: There is no budget set for this expense

# for the path please provide full path dir
project page url: https://roadmap.sh/projects/expense-tracker
