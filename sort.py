a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
t=[]
for i in c:
  t.append(i)
t.sort()
print(*t,end="")
