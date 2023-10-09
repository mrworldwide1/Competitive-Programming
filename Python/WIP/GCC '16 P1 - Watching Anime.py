totalHours = {}
N, A, C = (map(int, input().split()))

for hour in range(N):
    totalHours[hour+1] = "cannot"

for streaming in range(A):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai] = "can"
        ai+=1

for commitment in range(C):
    ci, di = (map(int, input().split()))
    while ci <= di:
        totalHours[ci] = "cannot"
        ci+=1

output = 0
for n in totalHours.values():
    if n == "can":
        output += 1

print(output)