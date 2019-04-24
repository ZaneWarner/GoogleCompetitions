cases = int(input())
for case in range(1, cases+1):
    A = ""
    B = ""
    N = input()
    for numeral in N:
        if numeral == "4":
            A += "3"
            B += "1"
        else:
            A += numeral
            B += "0"
    print("Case #{}: {} {}".format(case, A, B))
    