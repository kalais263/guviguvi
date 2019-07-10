a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
n=0
for i in range(0,a):
  if(c[i]%2==1):
    n=n+1
    if(n==b):
      print(c[i])
