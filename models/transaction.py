

#transaction class with attr amount, date, description
class Transaction:

    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        print(f"[{self.date}] | ${self.amount:.2f} | {self.description}") #[2024-03-15] | $250.00 | Freelance work payment



class Income(Transaction):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description)
        self.category = category

    def __str__(self)
        label = "[INCOME]"
        print(f"{label:<10} [{self.date}] | ${self.amount:>10,.2f} | {self.description:<30} | {self.category}") #[INCOME] [2024-03-15] | $250.00 | Freelance work payment | CATEGORY
   
class Expense(Transaction):
    def __init__(self, amount, date, description, category):
        super().__init__(amount,date,description)
        self.category = category

    def __str__(self):
        label = "[EXPENSE]"
        print(f"{label:<10} [{self.date}] | ${self.amount:>10,.2f} | {self.description:<30} | {self.category}") #[EXPENSE] [2024-03-15] | $250.00 | Freelance work payment | CATEGORY
