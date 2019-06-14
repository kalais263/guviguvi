a=int(input())
b=list(map(int,input().split()))
t=[]
for i in sorted(b):
  t.append(i)
c=min(t)
t.remove(c)
print(min(t))
