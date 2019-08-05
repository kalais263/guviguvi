a=int(input())
b=list(map(int,input().split()))[:a]
c=b.count(0)
e=0
t=[]
for i in b:
  if(i==0):
    e=e+1
  elif(e!=c and i==1):
    t.append(i)
print(*t,end="")
