totalHours = []
N, A, C = (map(int, input().split()))

for hour in range(N):
    totalHours.append(hour+1)

for stream in range(A):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai-1] = "y"
        ai+=1

for commit in range(C):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai-1] = ai
        ai+=1

print(totalHours.count("y"))