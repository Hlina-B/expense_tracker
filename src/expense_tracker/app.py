from expense_tracker.UI.cli import get_user_input
from expense_tracker.service.expense_tracker import dispatcher

def main():
    args = get_user_input()
    dispatcher(args)


if __name__ == "__main__":
    main()