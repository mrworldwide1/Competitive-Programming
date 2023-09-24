import sys

N = int(sys.stdin.readline())
C = int(sys.stdin.readline())*2
finalAns = ""

plants = list(map(int, sys.stdin.readline().split()))
ans = [plant + C for plant in plants]

for num in ans:
    finalAns += str(f"{num} ")

print(finalAns)