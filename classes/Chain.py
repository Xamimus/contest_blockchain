import hashlib
from classes.Block import Block
import string
import random
import os

class Chain:

    last_transaction_number = 0

    def __init__(self):
        self.blocks = os.listdir('content/blocs')

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

    def get_block(self):
        pass

    def add_transaction(self):
        pass

a = Chain()
a.generate_hash()