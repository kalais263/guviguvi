a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=sorted(c)
if a in d:
  if b in d:
    print("yes")
else:
  print("no")
