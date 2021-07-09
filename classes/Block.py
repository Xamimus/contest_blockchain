import hashlib
import json
import Wallet
import os

class Block:

    """ parent_hash = "" """

    transactions = []

    def __init__(self, base_hash=None, hash=None):
        self.size = self.get_weight()
        self.base_hash = base_hash
        if self.check_hash(base_hash) and self.load(hash):
            self.save()

    def check_hash(self, base_hash):
        self.hash = hashlib.sha256(base_hash.encode()).hexdigest()
        if self.hash[:4] == "0000":
            return True
        else:
            return False

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction():
        pass

    def get_weight(self):
        filename = "content/blocs/" + str(self.hash) + ".json"
        file_stats = os.stat(filename)
        return file_stats.st_size

    def save(self):
        data = {
            'base_hash': self.base_hash,
            'hash': self.hash,
            'parent_hash': self.parent_hash,
            'transactions': self.transactions
            }
        filename = "content/blocs/" + str(self.hash) + ".json"
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load(self, hash=None):
        if hash == None:
            return True
        else:
            filename = "content/wallets/" + str(hash) + ".json"
            with open(filename) as json_file:
                data = json.load(json_file)
                self.base_hash = data['base_hash']
                self.hash = data['hash']
                self.parent_hash = data['parent_hash']
                self.transactions = data['transactions']
            return False   
