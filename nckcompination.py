import math
a,b=list(map(int,input().split()))
n=math.factorial(a)
c=math.factorial(a-b)
d=math.factorial(b)
e=d*c
print(int(n/e))
