a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
s=[]
n=[]
c=0
for i in range(0,a):
  c=c+b[i]
  t.append(c)
s=t[::-1]
for i in range(0,a):
  n.append(t[i]+s[i])
print(*n,end="")
