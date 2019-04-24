import math
import string

class cryptopangram():
    def __init__(self, primeUpperBound, L):
        self.primeUpperBound = primeUpperBound
        self.L = L
        self.messageAsPossiblePrimes = [0]*L
        self.primesUsed = {}
        self.message = [0]*(L+1)
        self.out = ""
        
    def factor(self, numberToFactor):
        for p in range(2, self.primeUpperBound):
            q = numberToFactor/p
            if q == math.floor(q):
                return p, q
        
    def generatePossiblePrimes(self):
        composites = [int(s) for s in input().split(" ")]
        p, q = self.factor(composites[0])
        self.primesUsed[p] = 0
        self.primesUsed[q] = 0
        self.messageAsPossiblePrimes[0] = [p, q]
        for i in range(1, self.L):
            composite = composites[i]
            newFactor = composite/p
            if newFactor == math.floor(newFactor):
                q = newFactor
                self.primesUsed[q] = 0
            else:
                newFactor = composite/q
                p = newFactor
                self.primesUsed[p] = 0
            self.messageAsPossiblePrimes[i] = [p, q]
        
    def assignPrimes(self):
        primesList = []
        for prime in self.primesUsed:
            primesList.append(prime)
        primesList.sort()
        alphabet = string.ascii_uppercase
        for i in range(len(primesList)):
            self.primesUsed[primesList[i]] = alphabet[i]
            
    def decode(self):
        seeded = []
        for i in range(self.L):
            pair1 = self.messageAsPossiblePrimes[i]
            if pair1[0] == pair1[1]:
                self.message[i] = pair1[0]
                self.message[i+1] = pair1[0]
                seeded.append(i)
                seeded.append(i+1)
            elif i < self.L-1:
                pair2 = self.messageAsPossiblePrimes[i+1]
                pairElems = []
                for e in (pair1 + pair2):
                    if e not in pairElems:
                        pairElems.append(e)
                if len(pairElems) == 3:
                    for e in pairElems:
                        if e in pair1 and e in pair2:
                            self.message[i+1] = e
                            seeded.append(i+1)
        while seeded != []:
            seed = seeded.pop()
            if seed != 0: 
                if self.message[seed-1] == 0:
                    pair = self.messageAsPossiblePrimes[seed-1]
                    self.message[seed-1] = (pair[0]*pair[1])//self.message[seed]
                    seeded.append(seed-1)
            if seed != self.L:
                if self.message[seed+1] == 0:
                    pair = self.messageAsPossiblePrimes[seed]
                    self.message[seed+1] = (pair[0]*pair[1])//self.message[seed]
                    seeded.append(seed+1)
        for i in range(len(self.message)):
            self.out += self.primesUsed[self.message[i]]
        return self.out
        
    
            
                
cases = int(input())
for case in range(1, cases+1):
    N, L = [int(s) for s in input().split(" ")]
    x = cryptopangram(N, L)
    x.generatePossiblePrimes()
    x.assignPrimes()
    message = x.decode()
    print("Case #{}: {}".format(case, message))

# x = cryptopangram(103, 5)
# h = {}
# h[2] = "A"
# h[3] = "B"
# h[5] = "C"
# h[7] = "D"
# x.primesUsed = h
# x.messageAsPossiblePrimes = [[2,3],[3,3],[3,5],[5,7],[7,7]]
# x.decode()
# print(x.message)