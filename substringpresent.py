a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
d=list(map(int,input().split()))[:b]
n=0
for i in c:
  for i in d:
    n=n+1
if(n>=1):
  print("YES")
else:
  print("NO")
