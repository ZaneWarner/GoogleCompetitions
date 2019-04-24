cases, maxNights, maxGophers = [int(s) for s in input().split(" ")]
unfailed = True
for i in range(1, cases+1):
    blades = 2
    nights = 0
    gopherPossibilities = set()
    for i in range(1, maxGophers+1):
        gopherPossibilities.add(i)
    while nights < maxNights and unfailed:
        nights += 1
        out = str(blades)
        for _ in range(17):
            out += " "
            out += str(blades)
        print(out)
        intake = input()
        if intake == "-1":
            unfailed = False
        else:
            nums = [int(s) for s in intake.split(" ")]
            moved = sum(nums)
            newPossibilities = set()
            while moved <= maxGophers:
                newPossibilities.add(moved)
                moved += blades
            gopherPossibilities = gopherPossibilities.intersection(newPossibilities)
            blades += 1
            if blades > 18:
                blades = 2
            if len(gopherPossibilities) == 1:
                break
    if unfailed:
        for possibility in gopherPossibilities:
            print(str(possibility))
            break
        succeed = input()
        if succeed == "-1":
            unfailed = False
    