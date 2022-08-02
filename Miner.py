import hashlib
import random
import string
from time import sleep

class Miner :
    def __init__(self) -> None:
        pass
    def mint(self, previousHash, transaction):
        # rule: hash with 4 chua so dau = 0
        hash = hashlib.new('SHA256', 'hello'.encode()).hexdigest()
        while(hash[0:3] != "000") :
            randStr = "".join(random.choices(string.ascii_letters, k=10))
            hash = hashlib.new('SHA256', randStr.encode()).hexdigest()
            print(hash)
        return hash
        
        