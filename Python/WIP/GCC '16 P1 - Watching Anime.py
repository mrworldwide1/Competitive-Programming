totalHours = {}
N, A, C = (map(int, input().split()))

for hour in range(N):
    totalHours[hour+1] = "n"

for streaming in range(A):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai] = "y"
        ai+=1

for commitment in range(C):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai] = "n"
        ai+=1

print(list(totalHours.values()).count("y"))