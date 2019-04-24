class eating: 
    def __init__(self, stones):
        self.stones = stones
        self.secondsElapsed = 0
        self.energyGained = 0
        self.stoneQueue = []
    
    def consume(self):
        stone = self.stones[-1]
        self.energyGained += stone[1]
        del self.stones[-1] 
        self.secondsElapsed += 1
        
    def update(self):
        for stone in self.stones:
            stoneEnergy = max(stone[1] - (self.secondsElapsed*stone[0]), 0)
            stone[1] = stoneEnergy
            if stoneEnergy < stone[0]:
                stone[0] = stoneEnergy
        self.stones.sort()


cases = int(input())
for case in range(1, cases+1):
    stones = []
    numStones = int(input())
    for _ in range(numStones):
        S, E, L = [int(s) for s in input().split(" ")]
        stones.append([L*S, E])
    stones.sort()
    x = eating(stones)
    while x.stones != []:
        x.consume()
        x.update()
        
    print("Case #{}: {}".format(case, x.energyGained))
    
