cases = int(input())
for case in range(1, cases+1):
    r, c = [int(s) for s in input().split(" ")]
    grid = []
    for row in range(r):
        grid.append(list(input()))
    unusedRows = []
    for row in range(r):
        unusedSpaces = []
        letter = None
        for col in range(c):
            if grid[row][col] != "?":
                newLetter = grid[row][col]
                if letter == None:
                    for space in unusedSpaces:
                        grid[row][space] = newLetter
                letter = newLetter
            else:
                if letter != None:
                    grid[row][col] = letter
                else:
                    unusedSpaces.append(col)
        if letter == None:
            unusedRows.append(row)
        else:
            for unusedRow in unusedRows:
                for unusedCol in range(c):
                    grid[unusedRow][unusedCol] = grid[row][unusedCol]
            unusedRows = []
    for row in unusedRows:
        for col in range(c):
                grid[row][col] = grid[row-1][col]
    print("Case #{}:".format(case))
    for row in range(r):
        out = ''.join(grid[row])
        print(out)
        