a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
for i in range(0,b):
  c.insert(0,c.pop())
print(*c,end="")
