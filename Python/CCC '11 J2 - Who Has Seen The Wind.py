import math
import sys

h=float(input())
M=float(input())
t=1

while t <= M:
    if ((-6*(math.pow(t, 4)))+((h)*(math.pow(t, 3)))+(2*(math.pow(t, 2)))+t) <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        sys.exit()
    else:
        t+=1
print("The balloon does not touch ground in the given time.")