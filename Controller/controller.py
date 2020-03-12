from Model.blockchain import BlockChain
from Model.block import Block


class Controller:
    blockFund = BlockChain()

    blockFund.addBlock(Block(1, "03/09/2020", 1100))

    blockFund.addBlock(Block(1, "03/10/2020", 500))

    blockFund.addBlock(Block(1, "03/11/2020", 1800))

    for b in blockFund.chain:
        print(b)


