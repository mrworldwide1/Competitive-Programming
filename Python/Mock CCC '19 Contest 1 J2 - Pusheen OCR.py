S = input()
y = ["p", "u", "s", "h", "e", "e", "n"]
num = 0
count = 0
for i in S:
    if i != y[num]:
        count += 1
        num += 1
    else:
        num+=1

print(count)
