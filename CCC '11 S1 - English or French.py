N = int(input())
t=0
s=0

for i in range(N):
        t += word.count("t")
        t += word.count("T")
        s += word.count("s")
        s += word.count("S")

if t > s:
    print("English")
elif t < s:
     print("French")
elif t>=s:
     print("French")