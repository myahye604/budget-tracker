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

    def get_total_expenses(self):
        total_exp = 0
        for t in self._transactions:
            if t.__class__.__name__ == "Expense":
                total_exp += t.amount
        return total_exp
        
    def get_balance(self):
        totalexp = self.get_total_expenses()
        totalinc = self.get_total_income()
        balance = totalinc - totalexp
        return balance
    
    def get_all_transactions(self):
        print("/========================================== All Transactions ===========================================/")
        if not self._transactions:
            #empty list
            print("\nNo transactions currently, use options 2 and 3 to add a transaction.")
        else:
            for t in self._transactions:
                print(t)
        print("/=======================================================================================================/")
    
    def get_summary(self):
        totalexp = self.get_total_expenses()
        totalinc = self.get_total_income()
        balance = self.get_balance()
        print("/========================================= Budget Summary =============================================/")
        print(f"Total Income:    ${totalinc:>10,.2f}")
        print(f"Total Expenses:  ${-totalexp:>10,.2f}")
        print(f"Balance:         ${balance:>10,.2f}")
        print("/======================================================================================================/")
        print("\n\n")
        self.get_all_transactions()
           
        

