b=int(input())
a=0
c=0
for i in range(0,b):
  a=b%10
  b=b//10
  c=c+a*a
print(c)
