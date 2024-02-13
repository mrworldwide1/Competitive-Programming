import sys

t=0
s=0
text=[]

for i in range(int(sys.stdin.readline())):
    text.append(sys.stdin.readline().lower())

for word in text:
    t += word.count("t")
    s += word.count("s")

if t > s:
    print("English")
elif t < s:
     print("French")
elif t>=s:
     print("French")