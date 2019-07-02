a=int(input())
t=[]
for i in range(0,a):
  b=list(map(int,input().split()))
  for i in b:
    t.append(i)
  t.sort()
print(*t,end="")
