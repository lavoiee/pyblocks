import hashlib
import json

class Block():
    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calchash()

    def calchash(self):
        block_string = json.dumps({"nonce": self.nonce, "tstamp": self.tstamp,
                                   "transaction": self.transaction, "prevHash": self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string = "nonce :" + str(self.nonce)
        string += "tstamp :" + str(self.tstamp)
        string += "transaction :" + str(self.transaction)
        string += "prevhash: " + str(self.prevhash)
        string += "hash: " + str(self.hash)

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]
    def generateGenesisBlock(self):
        return Block(1, '03/09/2020', "In order for a slave to be free he must leave the plantation")
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash()
        newBlock.hash = newBlock.calchash()
        self.chain.append(newBlock)

blockFundCoin = BlockChain()

blockFundCoin.addBlock(Block(1, '03/09/2020', 1100))
blockFundCoin.addBlock(Block(1, '03/10/2020', 500))
blockFundCoin.addBlock(Block(1, '03/11/2020', 1800))

