import hashlib
import json
import colors


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

        string = "\033[01m" + "\033[32m" + "nonce :" + "\033[0m" + str(self.nonce) + "\n"
        string += "\033[01m" + "\033[32m" + "tstamp :" + "\033[0m" + str(self.tstamp) + "\n"
        string += "\033[01m" + "\033[32m" + "transaction :" + "\033[0m" + str(self.transaction) + "\n"
        string += "\033[01m" + "\033[32m" + "prevhash: " + "\033[36m" + str(self.prevhash) + "\n"
        string += "\033[01m" + "\033[32m" + "hash: " + "\033[36m" + str(self.hash) + "\n"

        return string


class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]

    def generateGenesisBlock(self):
        return Block(1, "03/09/2020", "In order for a slave to be free he must leave the plantation")

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calchash()
        self.chain.append(newBlock)


blockFund = BlockChain()

blockFund.addBlock(Block(1, "03/09/2020", 1100))

blockFund.addBlock(Block(1, "03/10/2020", 500))

blockFund.addBlock(Block(1, "03/11/2020", 1800))

for b in blockFund.chain:
    print(b)
