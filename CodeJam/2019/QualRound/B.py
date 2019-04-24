cases = int(input())
for case in range(1, cases+1):
    gridSize = int(input())
    takenPath = input()
    myPath = ""
    for step in takenPath:
        if step == "S":
            myPath += "E"
        else:
            myPath += "S"
    print("Case #{}: {}".format(case, myPath))