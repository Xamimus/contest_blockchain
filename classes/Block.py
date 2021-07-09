import hashlib
import json
import os

class Block:

    def __init__(self, parent_hash=None, base_hash=None, hash=None):
        self.parent_hash = parent_hash
        self.size = 0
        self.weight = 0
        self.base_hash = base_hash
        self.hash = hash
        self.transactions = []
        if self.check_hash() and self.load():
            self.save()

    def check_hash(self):
        if self.hash[:4] == "0000" and self.hash != None:
            return True
        else:
            return False

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.get_weight()
        self.save()

    def get_transaction():
        pass

    def get_weight(self):
        filename = "content/blocs/" + str(self.hash) + ".json"
        file_stats = os.stat(filename)
        self.weight = file_stats.st_size

    def save(self):
        data = {
            'base_hash': self.base_hash,
            'hash': self.hash,
            'parent_hash': self.parent_hash,
            'transactions': self.transactions,
            'weight': self.weight
            }
        filename = "content/blocs/" + str(self.hash) + ".json"
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load(self):
        if self.hash == None:
            return True
        else:
            try:
                filename = "content/blocs/" + str(self.hash) + ".json"
                with open(filename) as json_file:
                    data = json.load(json_file)
                    self.base_hash = data['base_hash']
                    self.hash = data['hash']
                    self.parent_hash = data['parent_hash']
                    self.transactions = data['transactions']
                    self.weight = data['weight']
            except:
                print("This block doesn't already exists. Creation of a new one...")
                return True
        return False