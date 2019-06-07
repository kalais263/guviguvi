a=input()
b=0
c=0
for i in a:
  if(i.isalpha()==True):
    b+=1
  elif(i.isdigit()==True):
    c+=1
if(b>=1 and c>=1):
  print("Yes")
else:
  print("No")
