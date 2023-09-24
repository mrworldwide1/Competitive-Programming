N = int(input())
C = int(input())*2

plants = list(map(int, input().split()))
# print(plants)
ans = [x + C for x in plants]

# if len(plants) == 1:
#         plants[0] += C
#         ans += str(f"{plants[0]} ")
#         print(ans)
# else:
#     for i in plants:
#         i += C
#         ans += i

print(str(ans).lstrip('[').rstrip(']'))