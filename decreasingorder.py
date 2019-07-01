a=int(input())
b=list(map(int,input().split()))[:a]
for i in range(0,a):
  c=max(b)
  print(c)
  b.remove(c)
