

#transaction class with attr amount, date, description
class Transaction:

    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self): #used so we can do print(class) and print function uses this as what to print
        return f"[{self.date}] | ${self.amount:>10,.2f} | {self.description:<30}" #[2024-03-15] | $250.00 | Freelance work payment



class Income(Transaction):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description)
        self.category = category

    def __str__(self):
        label = "[INCOME]"
        return f"{label:<10} [{self.date}] | ${self.amount:>10,.2f} | {self.description:<30} | {self.category}" #[INCOME] [2024-03-15] | $250.00 | Freelance work payment | CATEGORY
   
class Expense(Transaction):
    def __init__(self, amount, date, description, category):
        super().__init__(amount,date,description)
        self.category = category

    def __str__(self): 
        label = "[EXPENSE]"
        return f"{label:<10} [{self.date}] | ${-self.amount:>10,.2f} | {self.description:<30} | {self.category}" #[EXPENSE] [2024-03-15] | $250.00 | Freelance work payment | CATEGORY

# def main():
#     t = Transaction(250.00, "2025-03-15", "Test transaction")
#     print(f"/------Test transaction-----/\n{t}\n/-----------------------/")

#     i = Income(250.00, "2025-03-15", "Test transaction", "Warehouse Gig")
#     print(f"/------Test income-----/\n{i}\n/----------------/")

# if __name__ == "__main__": #so we don't run this anytime this file is imported, only if its run directly via python transaction.py (then __name__ == __main__)
#     main() 