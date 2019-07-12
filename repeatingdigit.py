a=input()
t=[]
c=0
for i in range(0,len(a)):
  t.append(i)
for i in t:
  for j in range(1,len(a)):
    if(i==j):
      c+=1
if(c>0):
  print("yes")
else:
  print("no")
