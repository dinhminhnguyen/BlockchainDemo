import hashlib

class InitBlock :
    totalAccount = 100
    def __init__(self, previousHash, blockId):
        self.blockId = blockId
        self.previousHash = previousHash
        self.nonce = 0

    def addTransaction(self, transactions):
        self.transactions = transactions
    
    def genHash(self):
        data = self.blockId
        self.hash = hashlib.sha256(str(data).encode('utf-8'))
    
    def getBalance(self):
        return self.totalAccount
    
    def show(self):
        print(self.previousHash)
        print(self.hash)
    




