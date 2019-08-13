a,b=input().split()
t=[]
if(len(a)>len(b)):
  c=len(a)-len(b)
  for i in range(1,c+1):
    b=b+str(i)
else:
  c=len(b)-len(a)
  for i in range(1,c+1):
    a=a+str(i)
for i in range(0,len(a)):
  t.append(a[i])
  t.append(b[i])
print(*t,sep="")
