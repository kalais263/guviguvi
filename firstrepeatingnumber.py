a=int(input())
b=list(map(int,input().split()))[:a]
for i in b:
  e=b.count(i)
  if(e==1):
    print(i)
  else:
    continue
