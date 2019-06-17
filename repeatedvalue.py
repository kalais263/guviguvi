a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
e=0
t=[]
for i in c:
  t.append(i)
for i in t:
  if(i==b):
    e=e+1
print(e)
