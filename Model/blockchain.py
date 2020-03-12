from Model.blocks import Block


class BlockChain:
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]

    def generateGenesisBlock(self):
        return Block(1, "03/09/2020", "In order for a slave to be free he must leave the plantation.")

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calchash()
        newBlock.blocknumber = len(self.chain)
        self.chain.append(newBlock)

