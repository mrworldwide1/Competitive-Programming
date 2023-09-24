import sys

N = int(sys.stdin.readline())
t=0
s=0
text=[]

for i in range(N):
    text.append(input().lower())

for word in text:
    t += word.count("t")
    s += word.count("s")

if t > s:
    print("English")
elif t < s:
     print("French")
elif t>=s:
     print("French")