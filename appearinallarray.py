a,b=list(map(int,input().split()))
n=[]
t=[]
for i in range(0,a):
  c=list(map(str,input().split()))[:b]
  d=set(c)
  for i in d:
    t.append(i)
for i in t:
  p=t.count(i)
  if(p==a):
    n.append(i)
print(*set(n),end="")
