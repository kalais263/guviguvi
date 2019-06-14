a,b=list(map(int,input().split()))
if(a>b):
  c=a
else:
  c=b
while(1):
  if(c%a==0 and c%b==0):
    print(c)
    break
c=c+1
