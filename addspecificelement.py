a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
n=0
for i in range(0,a):
  for j in range(1,a-1):
    s=c[i]+c[j]
    if(s==b):
      n=n+1
if(n>0):
  print("YES")
else:
  print("NO")
