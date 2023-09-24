for i in range(int(input())):
    N = (list(map(int, input().split())))
    if N[2] == N[1]*N[0]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")