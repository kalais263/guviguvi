a=input()
a=set(a)
a=list(a)
b=a.count('a')
c=a.count('b')
d=b+c
n=0
p=0
for i in a:
  if(i=='a' or i=='b'):
    n=n+1
  else:
    p=p+1
if(p==0):
  print("yes")
else:
  print("no")
  
