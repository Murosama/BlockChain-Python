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

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Current Hashes not equal")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Previous Hashes not equal")
                return False

        return True

    def __repr__(self):
        return "Blockchain: [{}]".format(', '.join(str(block) for block in self.chain))

# Example usage RA;
blockchain = Blockchain()
blockchain.add_block(Block(1, blockchain.get_latest_block().hash, "Transaction Data 1"))
blockchain.add_block(Block(2, blockchain.get_latest_block().hash, "Transaction Data 2"))

print(blockchain)
print("Blockchain valid?", blockchain.is_chain_valid())