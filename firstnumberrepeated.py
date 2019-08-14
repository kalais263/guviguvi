def find(a):
  c=set()
  for i in b:
    if i in c:
      return i
    else:
      c.add(i)
a=int(input())
b=list(map(int,input().split()))[:a]
print(find(a))
