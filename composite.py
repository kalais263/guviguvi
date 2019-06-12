a=int(input())
f=0
for i in range(1,a):
  if(a%i==0):
    f=i
if(f>1):
  print("yes")
else:
  print("no")
