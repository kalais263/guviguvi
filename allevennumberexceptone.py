a=int(input())
b=list(map(int,input().split()))[:a]
c=0
t=[]
s=[]
for i in range(0,a):
  if(b[i]%2==0):
    t.append(b[i])
  elif(b[i]%2==1):
    s.append(b[i])
if(len(t)==1):
  print(*t,end="")
elif(len(s)==1):
  print(*s,end="")
    
