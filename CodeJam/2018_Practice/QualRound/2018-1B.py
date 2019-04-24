cases = int(input())
for case in range(1, cases+1):
    listLen = int(input())
    numList = [int(s) for s in input().split(" ")]
    evens = []
    odds = []
    for i in range(listLen):
        if i%2 == 0:
            evens.append(numList[i])
        else:
            odds.append(numList[i])
    evens.sort()
    odds.sort()
    last = -1
    evensIdx = 0
    oddsIdx = 0
    fail = False
    for i in range(listLen):
        if i%2 == 0:
            curr = evens[evensIdx]
            evensIdx += 1
        else:
            curr = odds[oddsIdx]
            oddsIdx += 1
        if curr < last:
            fail = True
            failIdx = i-1
            break
        last = curr
    if fail == False:
        print("Case #{}: OK".format(case))
    else: print("Case #{}: {}".format(case, failIdx))         