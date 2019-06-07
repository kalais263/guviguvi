a=int(input())
b=0
c=1
for i in range(0,a):
  print(c,end=" ")
  temp=b+c
  b=c
  c=temp
