ph = []
[ph.append(input()) for n in range(4)]

if (ph[0] == "8" or ph[0] == "9") and (ph[3] == "8" or ph[3] == "9") and (ph[1] == ph[2]):
    print("ignore")
else:
    print("answer")