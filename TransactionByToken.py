class TransactionByToken:
    transactions = []
    type = '$'
    def transaction(self, fromId, toId, amount):
        self.fromId = fromId
        self.toId = toId
        self.amount = amount
    
    def getTransaction(self):
        return self
        