a,b=input().split()
c=0
t=[]
s=[]
for i in a:
  t.append(i)
for i in b:
  s.append(i)
for i in t:
  for j in s:
    if(i==j):
      print("yes")
      break
    elif(i!=j):
      print("no")
      break
  break
