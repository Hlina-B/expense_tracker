from expense_tracker.UI.cli import get_user_input
from expense_tracker.service.expense_tracker import dispatcher
from expense_tracker.service.budget_tracker import b_dispatcher
from expense_tracker.models.expnse_mc import Commands, BCommands

def main():
    args = get_user_input()
    try:
        Commands(args.command)
        dispatcher(args)
    except:
        print("coming to budget haha...")
        b_dispatcher(args)



if __name__ == "__main__":
    main()