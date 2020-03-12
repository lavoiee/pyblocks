import hashlib
import json


class Block:

    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calchash()
        self.blocknumber = 0

    def calchash(self):
        block_string = json.dumps({"nonce": self.nonce, "tstamp": self.tstamp,
                                   "transaction": self.transaction, "prevHash": self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):

        string = "\033[01m" + "\033[32m" + "Block Number :" + "\033[0m" + str(self.blocknumber) + "\n"
        string += "\033[01m" + "\033[32m" + "Nonce :" + "\033[0m" + str(self.nonce) + "\n"
        string += "\033[01m" + "\033[32m" + "Time Stamp :" + "\033[0m" + str(self.tstamp) + "\n"
        string += "\033[01m" + "\033[32m" + "Transaction :" + "\033[0m" + str(self.transaction) + "\n"
        string += "\033[01m" + "\033[32m" + "Previous Hash: " + "\033[36m" + str(self.prevhash) + "\n"
        string += "\033[01m" + "\033[32m" + "Hash: " + "\033[36m" + str(self.hash) + "\n"

        return string
