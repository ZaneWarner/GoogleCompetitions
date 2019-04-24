def calcDamage(seq, h):
    power = 1
    damage = 0
    shots = 0
    maxPower = 0
    for i in range(len(seq)):
        if seq[i] == "C":
            power += power
        if seq[i] == "S":
            damage += power
            if power not in h:
                h[power] = 1
            else:
                h[power] += 1
            shots += 1
            maxPower = power
    return damage, shots, maxPower
        
    

cases = int(input())
for case in range(1, cases+1):
    shield, sequence = input().split(" ")
    shield = int(shield)
    h = {}
    damage, shots, power = calcDamage(sequence, h)
    if shots > shield:
        print("Case #{}: IMPOSSIBLE".format(case))
    else:
        swaps = 0
        while damage > shield:
            halfpower = power//2
            if h[power] > 0:
                h[power] -= 1
                if halfpower in h:
                    h[halfpower] += 1
                else:
                    h[halfpower] = 1
                damage -= halfpower
                swaps += 1
            else:
                power = halfpower
        print("Case #{}: {}".format(case, swaps))

import numpy as np    
def randomTestCases():
    shield = np.random.randint(10**3)
    lenP = np.random.randint(2, 31)
    str = ""
    for i in range(lenP):
        flip = np.random.randint(1,3)
        if flip == 1:
            str += "C"
        else: str += "S"
    return shield, str

for i in range(20):
    s, st = randomTestCases()
    print("{} {}".format(s, st))
    
    