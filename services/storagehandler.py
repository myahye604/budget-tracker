from models.transaction import Income, Expense, Transaction
import json


class storageHandler:

    def __init__(self):
        pass
    

    def _seriailize(self, transactions): #converts list of transactions to json
        t_dict_list =  []
        for t in transactions:        
            t_dict = {'type':t.t.__class__.__name__,
                      'amount':t.amount, 
                      'date':t.date, 
                      'description':t.description, 
                      'category':t.category}
            t_dict_list.append(t_dict)
        return t_dict_list

    def _deserialize(self, json_transactions): #converts json into list of transactions
        t_transac_list = []
        for t in json_transactions:
            if json_transactions['type'] == "Income":
                i = Income(json_transactions['amount'], json_transactions['date'], json_transactions['description'], json_transactions['category'])
                t_transac_list.append(i)
            else:
                e = Expense(json_transactions['amount'], json_transactions['date'], json_transactions['description'], json_transactions['category'])
                t_transac_list.append(e)
        return t_transac_list

    def save(self, transactions): #saves list of transactions, writes to data.json
        data = self._seriailize(self, transactions)
        t_json = json.dumps(data)
        try:
            with open("data.json", "a") as f:
                f.write(t_json) #if file exists
        except FileNotFoundError:
            newFile = open("data.json", "w") #otherwise create new file 
            newFile.write(t_json)
            #save to new json file

    def load(self): #loads data.json, returns list of Transaction obj
        _transactions = []
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
            _transactions =self._deserialize(self, data)
        except:
            print("No transactions currently..")
        return _transactions
    