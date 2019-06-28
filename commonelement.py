a=int(input())
b=list(map(str,input().split()))[:a]
c=list(map(str,input().split()))[:a]
t=[]
d=[]
for i in b:
  t.append(sorted(i))
for j in c:
  d.append(sorted(j))
for i in t:
  for j in d:
    if(i==j):
      print(*i,end=" ")
      d.remove(i)
