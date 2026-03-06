from para import *
from General import *

class Generator:
    def __init__(self,key):
        self.init=[key[0:32]^fki[0],key[32:64]^fki[1],key[64:96]^fki[2],key[96:128]^fki[3]]
        self.keylis=self.init

    def genkey(self,round):
        proc1=self.keylis[round+1]^self.keylis[round+2]^self.keylis[round+3]^cki[round]
        proc2=sbox[proc1[0:8]]+sbox[proc1[8:16]]+sbox[proc1[16:24]]+sbox[proc1[24:32]]
        fproc=proc2^CircularRotation.left(proc2,13)^CircularRotation.left(proc2,23)#<<符号不是循环左移，这里需要后续的改进
        roundkey=fproc^self.keylis[round]
        self.updatekey(roundkey)
        return roundkey

    def updatekey(self,key):
        self.keylis=[self.keylis[1],self.keylis[2],self.keylis[3],key]
