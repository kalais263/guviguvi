a,b=list(map(str,input().split()))
b=int(b)
t=[]
a=a[::-1]
for i in range(0,b):
  t.append(a[i])
t=t[::-1]
print(*t,sep="")
