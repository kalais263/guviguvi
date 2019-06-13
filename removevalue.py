a,b=input().split()
c=list(map(str,input().split()))
d=[]
for i in c:
  d.append(i)
  if b in d:
    d.remove(b)
print(*d,sep=" ")
  
