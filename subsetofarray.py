a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
d=list(map(int,input().split()))[:b]
n=0
for i in d:
  if  i in c:
    n=n+1
if(n==len(d)):
  print("YES")
else:
  print("NO")
