def flip(pancakes, flipper, i):
    for j in range(i, i+flipper):
        if pancakes[j] == "+":
            pancakes[j] = "-"
        else: pancakes[j] = "+"
    return pancakes

cases = int(input())
for case in range(1, cases+1):
    inputStr = input()
    print(inputStr)
    pancakes, flipper = inputStr.split(" ")
    flipper = int(flipper)
    flips = 0
    for i in range(len(pancakes)+1-flipper):
        if pancakes[i] == "-":
            pancakes = flip(pancakes, flipper, i)
            flips += 1
    if pancakes == "+"*len(pancakes):
        print("Case #{}: {}".format(case, flips))
    else: print("Case #{}: IMPOSSIBLE".format(case))