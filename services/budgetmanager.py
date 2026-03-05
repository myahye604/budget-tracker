from models.transaction import Transaction, Income, Expense


class BudgetManager:

    def __init__(self):
        self._transactions = [] #list of Transactions, which are either of type income or expense

    def add_transaction(self, _sTransaction):
        self._transactions.append(_sTransaction) # type: ignore

    def get_total_income(self):

        #for every transaction in our list, if it is of type income, we add the amounts
        total_inc = 0
        for t in self._transactions:
            if t.__class__.__name__ == "Income": #only add if type is income
                total_inc += t.amount 
        return total_inc

    # def get_total_expenses(self):

    # def get_balance(self):

    # def get_summary(self):

