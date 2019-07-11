a=input()
t=[]
for i in a:
  if(i.isdigit()==True):
    t.append(i)
print(*t,sep="")
