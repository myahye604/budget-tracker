from models.transaction import Income, Expense
from services.budgetmanager import BudgetManager
from services.storagehandler import storageHandler
from datetime import date

def main_menu():
    print("""======= Budget Tracker =======
            1. Add Income
            2. Add Expense
            3. View Summary
            4. View All Transactions
            5. Quit
==============================""")
    


def main():

    sHandler = storageHandler(r"C:\Users\moman\Documents\LearningCode\budget-tracker\data\data.json")
    manager = BudgetManager(sHandler)

    # # Income transactions
    # i1 = Income(2500.00, "2025-03-15", "March salary", "Salary")
    # i2 = Income(750.00, "2025-03-18", "Freelance gig", "Freelance")
    # i3 = Income(200.00, "2025-03-20", "Stock dividend", "Investment")

    # # Expense transactions
    # e1 = Expense(84.50, "2025-03-16", "Weekly groceries", "Food")
    # e2 = Expense(1200.00, "2025-03-01", "Monthly rent", "Rent")
    # e3 = Expense(45.00, "2025-03-17", "Bus pass", "Transport")

    # # Add to manager
    # manager.add_transaction(i1)
    # manager.add_transaction(i2)
    # manager.add_transaction(i3)
    # manager.add_transaction(e1)
    # manager.add_transaction(e2)
    # manager.add_transaction(e3) #at this point our data.json will be populated with these

    _userInput = 1
    while(_userInput != "5"):
        main_menu()
        _date = date.today().strftime("%Y-%m-%d")

        _userInput = input("\nEnter your choice: ")
        if _userInput == "1": #add income
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            incomeT = Income(amount, _date, description, category)
            manager.add_transaction(incomeT)
            print("\n\n")
        elif _userInput == "2": #add expense
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            expenseT = Expense(amount, _date, description, category)
            manager.add_transaction(expenseT)
            print("\n\n")
        elif _userInput == "3": #View Summary
            manager.get_summary()
            print("\n\n")
        elif _userInput == "4": #View transations
            manager.get_all_transactions()
            print("\n\n")
        elif _userInput == "5": #quit
            print("\n\nGoodbye!\n\n")
        else: #incorrect input
            print("Incorrect input, reposting main menu..\n\n")
            print("\n\n")



if __name__ == "__main__":
    main()
          