from InitBlock import InitBlock
import hashlib
import rsa
from TransactionByToken import TransactionByToken
from Miner import Miner

class BlockChain:
    def __init__(self) -> None:
        self.chain = []

    def getBlock(self, blockId):
        return self.chain[blockId]
    
    def main():
        privateKey, publicKey = rsa.newkeys(512)
        x = rsa.encrypt("hello".encode(), privateKey)
        print(x)
        y = rsa.decrypt(x, publicKey)
        print(y)

        intRoot = "initblock"
        rootHash = hashlib.sha256(intRoot.encode('utf-8')).hexdigest()

        transactionByToken = TransactionByToken()
        transactionByToken.transaction(0, 1, 5)
        A1 = transactionByToken.getTransaction()
        transactionByToken.transaction(0,2, 6)
        A2 = transactionByToken.getTransaction()
        
        A = InitBlock(rootHash, 0)
        A.addTransaction([A1, A2])
        A.genHash()
        B = InitBlock(A.hash, 1)
        B.addTransaction([A1, A2])
        B.genHash()
        C = InitBlock(B.hash, 2)
        C.addTransaction([A1, A2])
        C.genHash()
        miner = Miner()
        newHash = miner.mint(B.hash, A1)

    if __name__=="__main__":
        main()

