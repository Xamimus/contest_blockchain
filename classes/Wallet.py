import uuid
import json

class Wallet:

    def __init__(self, id=None):
        if self.load(id):
            self.unique_id = self.generate_unique_id()
            self.balance = 100
            self.history = []
            self.save()

    def generate_unique_id(self):
        notChecked = True
        while notChecked:
            id = uuid.uuid4().int
            filename = "content/wallets/" + str(id) + ".json"
            try:
                with open(filename): pass
            except IOError:
                notChecked = False       
        return id

    def add_balance(self, int):
        self.balance += int
        self.save()

    def sub_balance(self, int):
        self.balance -= int
        self.save()

    def send():
        pass

    def save(self):
        data = {
            'unique_id': self.unique_id,
            'balance': self.balance,
            'history': self.history
            }
        filename = "content/wallets/" + str(self.unique_id) + ".json"
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load(self, id=None):
        if id == None:
            print("Wallet doesn't exists. Creation of a new one...")
            return True
        else:
            filename = "content/wallets/" + str(id) + ".json"
            with open(filename) as json_file:
                data = json.load(json_file)
                self.unique_id = data['unique_id']
                self.balance = data['balance']
                self.history = data['history']
            return False   

    def add_history(self, transaction_id):
        self.history.append(transaction_id)

