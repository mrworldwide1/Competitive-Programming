part1 = "A long time ago in a galaxy "
part2 = "away..."
count = ""

N = int((input()))

for i in range(N):
  if i <= N-2:
    count += "far, "
  else:
    count += "far "
    
print(part1 + count + part2)