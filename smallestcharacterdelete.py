a,b=list(map(str,input().split()))
c=a
t=[]
w=str()
for i in c:
  t.append(i)
if(len(t)>1):
  t.pop(-1)
for i in t:
  w=w+i
d=w+b
print(d)
