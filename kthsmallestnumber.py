a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
for i in range(0,b-1):
  c.remove(min(c))
print(min(c))
