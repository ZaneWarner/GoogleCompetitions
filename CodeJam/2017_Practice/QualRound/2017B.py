

cases = int(input())
for case in range(1, cases+1):
    N = str(input())
    tidy = True
    last = 0
    untidyAfter = 0
    for i in range(len(N)):
        if int(N[i]) < last:
            untidyAfter = i-1
            tidy = False
            while N[untidyAfter] == N[untidyAfter-1] and untidyAfter > 0:
                untidyAfter -= 1
            break
        last = int(N[i])
    N_out = ""
    if not tidy:
        for i in range(len(N)):
            if i == untidyAfter:
                N_out += str(int(N[i]) - 1)
            elif i > untidyAfter:
                N_out += "9"
            else: N_out += N[i]
    else: N_out = N
    N_out = str(int(N_out))
    print("Case #{}: {}".format(case, N_out))
    
    