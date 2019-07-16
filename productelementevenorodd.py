a=int(input())
b=list(map(int,input().split()))[:a]
c=1
for i in b:
  c=c*i
if(c%2==0):
  print("even")
else:
  print("odd")
