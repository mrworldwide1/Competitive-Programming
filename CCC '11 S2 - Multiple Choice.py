N = int(input())
student_ans = []
teacher_ans = []
i = 0
stud_i = 0
C = 0

# the lines after N are 2N, wo we use two while loops. One for the first half of 2N and one for the other half.
while i < N:
    student_ans.append(input())
    i+=1

i = 0

while i < N:
    teacher_ans.append(input())
    i+=1

# SS from grass problem solving method
for _ in range(N):
    if student_ans[stud_i] == teacher_ans[stud_i]:
        C += 1
        stud_i += 1
    else:
        stud_i += 1

print(C)