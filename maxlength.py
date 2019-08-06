a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
for i in b:
  c=b.count(i)
  t.append(c)
print(max(t))
