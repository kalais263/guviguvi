a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
d=list(map(int,input().split()))[:b]
t=[]
for i in c:
  t.append(i)
for j in d:
  t.append(j)
t.sort()
print(*t,end="")
