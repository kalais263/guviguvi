import math
a,b=list(map(int,input().split()))
n=math.factorial(a)
c=math.factorial(a-b)
print(int(n/c))
