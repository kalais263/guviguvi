a=list(map(str,input().split()))
t=[]
for i in a:
  if((a.index(i)+1)==1 or (a.index(i)+1)%2==1):
    b=i[::-1]
    t.append(b)
  else:
    t.append(i)
print(*t,end=" ")
