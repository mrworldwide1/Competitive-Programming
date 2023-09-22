N = int(input())
C = int(input())*2
ans = ""

plants = list(map(int, input().split()))

if len(plants) == 1:
        plants[0] += C
        ans += str(f"{plants[0]} ")
        print(ans)
else:
    for i in plants:
            plants[i-1] += C
            ans += str(f"{plants[i-1]} ")

print(ans)