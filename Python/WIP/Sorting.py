number = int(input())
list = []

for n in range(number):
    list.append(int(input()))

list.sort()

for ans in list:
    print(ans)