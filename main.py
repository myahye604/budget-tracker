from models.transaction import Income, Expense
from services.budgetmanager import BudgetManager



def main():

    manager = BudgetManager()

    # Income transactions
    i1 = Income(2500.00, "2025-03-15", "March salary", "Salary")
    i2 = Income(750.00, "2025-03-18", "Freelance gig", "Freelance")
    i3 = Income(200.00, "2025-03-20", "Stock dividend", "Investment")

    # Expense transactions
    e1 = Expense(84.50, "2025-03-16", "Weekly groceries", "Food")
    e2 = Expense(1200.00, "2025-03-01", "Monthly rent", "Rent")
    e3 = Expense(45.00, "2025-03-17", "Bus pass", "Transport")

    # Add to manager
    manager.add_transaction(i1)
    manager.add_transaction(i2)
    manager.add_transaction(i3)
    manager.add_transaction(e1)
    manager.add_transaction(e2)
    manager.add_transaction(e3)

    # Test get_total_income
    print(f"Total Income: ${manager.get_total_income():,.2f}")

if __name__ == "__main__":
    main()
          