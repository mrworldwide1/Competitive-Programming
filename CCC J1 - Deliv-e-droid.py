# pseudo code
# totalPoints = 50*p - 10*c
# bonus points
# if p > c:
# totalPoints += 500

P = int(input())
C = int(input())

score = 0
score += P*50
score -= C*10

if P>C:
    score += 500

print(score)
