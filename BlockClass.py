import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = "{}{}{}{}".format(self.index, self.previous_hash, self.transactions, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return "Block(index: {}, previous_hash: {}, transactions: {}, timestamp: {}, hash: {})".format(
            self.index, self.previous_hash, self.transactions, self.timestamp, self.hash)
    
          

# Example usage RA;
block = Block(1, '0', 'Some transactions')
print(block)