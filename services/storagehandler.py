from models.transaction import Income, Expense, Transaction
import json


class storageHandler:

    def __init__(self, fpath):
        self._filepath = fpath
    

    def _seriailize(self, transactions): #converts list of transactions to json
        t_dict_list =  []
        for t in transactions:        
            t_dict = {'type':t.__class__.__name__,
                      'amount':t.amount, 
                      'date':t.date, 
                      'description':t.description, 
                      'category':t.category}
            t_dict_list.append(t_dict)
        return t_dict_list

    def _deserialize(self, json_list): #converts json into list of transactions
        t_transac_list = []   #json_transactions is list of json objests, ie [{json},{json2},..]
        for json_transactions in json_list:
            if json_transactions["type"] == "Income":
                i = Income(json_transactions['amount'], json_transactions['date'], json_transactions['description'], json_transactions['category'])
                t_transac_list.append(i)
            else:
                e = Expense(json_transactions['amount'], json_transactions['date'], json_transactions['description'], json_transactions['category'])
                t_transac_list.append(e)
        return t_transac_list

    def save(self, transactions): #saves list of transactions, writes to data.json
        data = self._seriailize(transactions)
        t_json = json.dumps(data)
        try:
            with open(self._filepath, "w") as f:
                f.write(t_json) #if file exists
            print(f"transaction is being added to file via save..")
            transactions.__str__()
        except FileNotFoundError:
            newFile = open(self._filepath, "w") #otherwise create new file 
            newFile.write(t_json)
            #save to new json file

    def load(self): #loads data.json, returns list of Transaction obj
        _transactions = []
        #print("in load function..")
        #print(f"filepath: {self._filepath}")
        try:
            with open(self._filepath, "r") as f:
                data = json.load(f)
            _transactions =self._deserialize(data)
            # #print("loading all current transactions in file...")
            # for t in _transactions:
            #     print(t)
        except Exception as e:
            print(f"[DEBUG] Load failled due to: {e}")
        return _transactions
    