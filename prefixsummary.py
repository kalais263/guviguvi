a=int(input())
b=list(map(int,input().split()))[:a]
c=0
t=[]
for i in range(0,a):
  c=c+b[i]
  t.append(c)
print(*t,end="")
