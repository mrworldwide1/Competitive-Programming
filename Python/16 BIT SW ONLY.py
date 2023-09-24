for i in range(int(input())):
    a = (list(map(int, input().split())))
    if a[2] == a[1]*a[0]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")