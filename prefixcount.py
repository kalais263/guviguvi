a=int(input())
b=list(map(str,input().split()))[:a]
c=input()
d=0
for i in range(0,a):
  if(b[i].startswith(c)):
    d=d+1
print(d)
