a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
n=1
for i in b:
  n*=i
for i in b:
  s=n//i
  t.append(s)
print(*t,end="")
