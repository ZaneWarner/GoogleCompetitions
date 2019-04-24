def neighbors(square, rows, cols):
    r = square[0]
    c = square[1]
    candidates = []
    if r-1 >= 0:
        candidates.append((r-1,c))
    if r+1 < rows:
        candidates.append((r+1,c))
    if c-1 >= 0:
        candidates.append((r,c-1))
    if c+1 < cols:
        candidates.append((r,c+1))
    return candidates
 
cases = int(input())
for case in range(cases):
    rows, cols = [int(s) for s in input().split(" ")]
    found = False
    pre = []
    post = []
    visitCount = 0
    visited = set()
    dist = 0
    for r in range(rows):
        row = list(input())
        for c in range(cols):
            if row[c] == "1":
                pre.append((r,c))
                visited.add((r,c))
                visitCount += 1
    while visitCount < rows*cols:
        dist += 1
        for square in pre:
            candidates = neighbors(square, rows, cols)
            for candidate in candidates:
                if candidate not in visited:
                    post.append(candidate)
                    visited.add(candidate)
                    visitCount += 1
        pre = post
        post = []
    maxima = pre
    maximaDist = dist
    numMaxima = len(pre)
    visitedByMaxima = {}
    maxID = 0
    for maximum in maxima:
        maxID += 1
        dist = maximaDist
        while dist > 0 and not found:
            for square in pre:
                if not found:
                    candidates = neighbors(square, rows, cols)
                    for candidate in candidates:
                        if candidate not in visitedByMaxima:
                            post.append(candidate)
                            visitedByMaxima[candidate] = [maxID]
                            if len(visitedByMaxima[candidate]) == numMaxima:
                                found = True
                                print("Case #{}: {}".format(case, dist))
                                break
                        elif maxID not in visitedByMaxima[candidate]:
                            post.append(candidate)
                            visitedByMaxima[candidate].append(maxID)
                            if len(visitedByMaxima[candidate]) == numMaxima:
                                found = True
                                print("Case #{}: {}".format(case, dist))
                                break
            dist -= 1
            pre = post
            post = []