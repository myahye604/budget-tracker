from models.transaction import Transaction, Income, Expense
from services.storagehandler import storageHandler

class BudgetManager:

    

    def __init__(self, storage):
        self._storage = storage
        self._transactions = storage.load() #loads current list of transactions, if nothing method returns empty list

    def add_transaction(self, _sTransaction):
        self._transactions.append(_sTransaction) # type: ignore
        self._storage.save(self._transactions)

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

