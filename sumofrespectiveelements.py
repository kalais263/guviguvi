a=int(input())
b=list(map(int,input().split()))[:a]
c=list(map(int,input().split()))[:a]
t=[]
for i in range(0,a):
  d=b[i]+c[i]
  t.append(d)
print(*t,end="")
