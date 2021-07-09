import hashlib
import Block
import string
import random

class Chain:
    blocks = []

    last_transaction_number = 0

    def __init__(self):
        pass

    def generate_hash(self):
        hash = ""
        while not self.verify_hash(hash):
            random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            hash = hashlib.sha256(random_str.encode()).hexdigest()
        print(random_str)

    def verify_hash(self, hash):
        if hash[:4] == "0000":
            return True
        else:
            return False

    def add_block(self, hash):
        new_block = Block(hash)
        self.blocks.append(new_block)

    def get_block(self):
        pass

    def add_transaction(self):
        pass

a = Chain()
a.generate_hash()