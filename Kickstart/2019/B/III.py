cases = int(input())
for case in range(1, cases+1):
    N, S = [int(s) for s in input().split(" ")]
    numbers = [int(s) for s in input().split(" ")]
    S += 1
    max = 0
    for start in range(N):
        end = start
        brought = 0
        h = {}
        while end < N:
            elem = numbers[end]
            if elem in h:
                h[elem] += 1
            else: h[elem] = 1
            if h[elem] <= S:
                brought += 1
            if h[elem] == S:
                brought -= S
            if brought > max:
                max = brought
            end += 1
    print("Case #{}: {}".format(case, max))