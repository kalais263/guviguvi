import math
a,b=list(map(int,input().split()))
c=a*b
d=int(math.sqrt(c))
if(c==d*d):
  print("yes")
else:
  print("no")
