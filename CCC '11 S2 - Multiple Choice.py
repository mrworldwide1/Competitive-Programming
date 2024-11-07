N = int(input())
student_ans = []
teacher_ans = []
i = 0
# i for student answers, j for teacher answers, need two varaibles otherwise this first while loop while evaluate to False and skip past teacher answers, returning C.

while i < N:
    student_ans.append(input())
    i+=1

i = 0

while i < N:
    teacher_ans.append(input())
    i+=1
print(student_ans, teacher_ans)
# since 2N lines after N, we can use range() function and plug in 2N//2