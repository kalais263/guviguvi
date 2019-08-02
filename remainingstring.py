a=input()
t=[]
for i in a:
  b=a.count(i)
  if(b==1):
    t.append(i)
print(*t,sep="")
