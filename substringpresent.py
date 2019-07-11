a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
d=list(map(int,input().split()))[:b]
for i in c:
  if i in d:
    print("YES")
    break
  else:
    print("NO")
    break
