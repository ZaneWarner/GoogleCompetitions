import collections

cases = int(input())
for case in range(1, cases+1):
    stalls, users = [int(s) for s in input().split(" ")]
    trackUsers = [0]*(stalls+1)
    trackUsers[stalls] = 1
    stallsQueue = collections.deque()
    visited = {}
    while users > 0:
        if stalls not in visited:
            visited[stalls] = 1
        if stalls%2 == 1:
            odd = True
        else: odd = False
        if odd:
            newStalls = stalls//2
            trackUsers[newStalls] += trackUsers[stalls]*2
            users -= trackUsers[stalls]
            minDist = newStalls
            maxDist = newStalls
            stallsQueue.append(newStalls)
        else:
            newStalls = (stalls//2)-1
            trackUsers[newStalls] += trackUsers[stalls]
            trackUsers[newStalls+1] += trackUsers[stalls]
            users -= trackUsers[stalls]
            minDist = newStalls
            maxDist = newStalls+1
            stallsQueue.append(newStalls+1)
            stallsQueue.append(newStalls)
        stalls = stallsQueue.popleft()
        while stalls in visited:
            stalls = stallsQueue.popleft()
    print("Case #{}: {} {}".format(case, maxDist, minDist))
            