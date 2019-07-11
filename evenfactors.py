n=int(input())
t=[]
a=[]
for i in range(1,n+1):
  if(n%i==0):
    t.append(i)
for i in t:
  if(i%2==0):
    a.append(i)
print(*a,end="")
  
