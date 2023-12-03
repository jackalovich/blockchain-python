from hashlib import sha256

# Function to update the hash using SHA-256
def updatehash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)
    
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

# Block class representing a block in the blockchain
class Block():
    def __init__(self, number=0, data=None, hash=None, nonce=0, previous_hash="0"*64):
        # Block attributes
        self.number = number
        self.data = data
        self.hash = hash
        self.nonce = nonce
        self.previous_hash = previous_hash
    
    def __str__(self):
        # String representation of the block for easy printing
        return f"Block #: {self.number}\n Hash: {self.hash}\n Previous: {self.previous_hash}\n Data: {self.data}\n Nonce: {self.nonce}\n"

    def calculate_hash(self):
        # Calculate the hash of the block
        return updatehash(self.previous_hash,
                        self.number,
                        self.data,
                        self.nonce)

# Blockchain class managing the chain of blocks
class Blockchain():
    def __init__(self, difficulty=4, chain=[]):
        # Initialize the blockchain with a specified difficulty and an empty chain
        self.difficulty = difficulty
        self.chain = chain

    def add_block(self, block):
        # Add a block to the blockchain
        self.chain.append({'hash': block.calculate_hash(),
                           'previous': block.previous_hash,
                           'data' : block.data,
                           'nonce': block.nonce})

    def mine_block(self, block):
        # Mine a block and add it to the blockchain
        try:
            block.previous_hash = self.chain[-1].get('hash')
        except IndexError:
            pass

        while True:
            if block.calculate_hash()[:self.difficulty] == '0' * self.difficulty:
                self.add_block(block)
                break
            else:
                block.nonce += 1

def main():
    # Main function to demonstrate the blockchain
    blockchain = Blockchain(difficulty=5)
    database = ['hello', 'btc', 'transaction']
    num = 0
    for data in database:  
        num += 1
        blockchain.mine_block(Block(num, data))
        
    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    main()
