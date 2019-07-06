a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
t=[]
for i in c:
  t.append(i)
for i in range(0,b-1):
  t.remove(max(t))
print(max(t))
