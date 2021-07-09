from classes.Wallet import Wallet
import hashlib
from classes.Block import Block
import string
import random
import os

class Chain:

    last_transaction_number = 0

    def __init__(self):
        self.blocks = os.listdir('content/blocs')
        self.transaction_id = 0

    def generate_hash(self):
        hash = ""
        while not self.verify_hash(hash):
            random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            hash = hashlib.sha256(random_str.encode()).hexdigest()
        self.base_hash = random_str
        self.hash = hash
        self.add_block()

    def verify_hash(self, hash):
        if hash[:4] == "0000":
            return True
        else:
            return False

    def add_block(self):
        new_block = Block(self.blocks[len(self.blocks) - 1], self.base_hash, self.hash)
        new_block.get_weight()
        new_block.save()
        self.blocks.append(new_block)

    def get_block(self, hash):
        filename = "content/blocs/" + str(hash) + ".json"
        try:
            with open(filename): 
                return Block(None, None, hash)
        except IOError:
            print("This block probably doesn't exists.")

    def add_transaction(self, saler_id, client_id, amount):
        saler = Wallet(saler_id)
        client = Wallet(client_id)
        if saler.load(saler_id) == False and client.load(client_id) == False:
            if client.balance > amount:
                i = 0
                while i < (len(self.blocks)):
                    current_block = self.get_block(self.blocks[i].replace('.json', ''))
                    if current_block.weight < 256000:
                        transaction = {
                            "id": self.get_transaction_id(),
                            "saler": saler.unique_id,
                            "client": client.unique_id,
                            "amount": amount
                        }
                        current_block.add_transaction(transaction)
                        saler.add_balance(amount)
                        client.sub_balance(amount)
                        print("Transaction succeed !")
                        return True
                    else:
                        i += 1
                self.add_block()
                transaction = {
                            "id": self.get_transaction_id(),
                            "saler": saler.unique_id,
                            "client": client.unique_id,
                            "amount": amount
                        }
                current_block.add_transaction(transaction)
                saler.add_balance(amount)
                saler.add_history(transaction["id"])
                client.add_history(transaction["id"])
                client.sub_balance(amount)
                print("Transaction succeed !")
                return True
            else:
                print("Transaction failed. Current balance of the receiver is insufficient")
                return False
        else:
            print("Transaction failed. Please check the wallet's ids validities.")
            return False

    def get_transaction_id(self):
        for b in self.blocks:
            hash = b.replace(".json", "")
            block = self.get_block(hash)
            self.transaction_id += len(block.transactions)
            print("Transaction's id : " + str(self.transaction_id))
        return self.transaction_id
