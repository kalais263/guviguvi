a=input()
b=0
for i in a:
  if i.isalpha():
    b=b+1
if(b>0):
  print("no")
else:
  print("yes")
