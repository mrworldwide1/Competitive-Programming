m = int(input()); n = int(input())
mNumbs =[]
nNumbs =[]
ways = 0

for num in range(m):
    mNumbs.append(num+1)

for num in range(n):
    nNumbs.append(num+1)
nNumbs.reverse()

i=0
while i < :
    if mNumbs[i] + nNumbs[i] == 10:
        ways += 1
    else:
        pass

if ways == 0:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {ways} ways to get the sum 10.")
