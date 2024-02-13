binaryList=[];memeList=""
for t in range(int(input())):
  binary = (format(int(input()), 'b'))
  for digit in str(binary):
      binaryList.append(digit)
  for num in binaryList:
    if num == "1":
        memeList+="dank "
    else:
        memeList+="meme "
  print(memeList);binaryList=[];memeList = ""