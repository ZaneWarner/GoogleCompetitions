import math

class Orchard():
    def __init__(self, M, botEdge, rightEdge):
        self.M = M
        self.botEdge = botEdge
        self.rightEdge = rightEdge
        self.minInZone = 0
    
    def scan(self):
        target = None
        for i in range(1, self.botEdge-1):
            if target != None:
                break
            for j in range(1, self.rightEdge-1):
                if target == None:
                    if self.zone(i, j) == self.minInZone:
                        target = [i, j]
                else:
                    break
                
        if target == None:
            self.minInZone += 1
            target = self.scan()
        return target
    
    def zone(self, i, j):
        found = 0
        for m in [i-1, i, i+1]:
            for n in [j-1, j, j+1]:
                found += self.M[m][n]
        return found
    
    def update(self, hit):
        i = hit[0]
        j = hit[1]
        repeat = False
        if M[i][j] == 1:
            repeat = True
        M[i][j] = 1
        return repeat
        

cases = int(input())
for case in range(cases):
    fail = False
    succeed = False
    area = int(input())
    filled = 0
    shot = 0
    botEdge = math.floor(math.sqrt(area))
    rightEdge = math.ceil(area/botEdge)
    M = [ [0]*(rightEdge) for _ in range(botEdge)]
    mustFill = botEdge * rightEdge
    x = Orchard(M, botEdge, rightEdge)
    while filled < mustFill and shot<1000 and not fail and not succeed:
        target = x.scan()
        repeat = True
        while repeat and shot<1000:
            print("{} {}".format(target[0]+1, target[1]+1), flush=True)
            shot += 1
            hit = [int(s) for s in input().split(" ")]
            for i in range(len(hit)):
                hit[i] -= 1
            if hit == [-1, -1]:
                succeed = True
                break
            if hit == [-2, -2]:
                fail = True
                break
            repeat = x.update(hit)
            if not repeat:
                filled += 1
    if fail == True:
        break
        
