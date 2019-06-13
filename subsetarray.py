a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in c:
  for j in d:
    if(i==j):
      print("yes")
      break
    else:
      print("no")
  break
