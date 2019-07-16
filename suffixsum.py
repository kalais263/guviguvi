a=int(input())
b=list(map(int,input().split()))[:a]
c=0
t=[]
for i in range(0,a):
  c=c+b[i]
  t.append(c)
t=t[::-1]
print(*t,end="")
