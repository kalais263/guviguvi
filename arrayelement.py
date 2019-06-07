num=int(input())
val=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(val)):
    if(i%2==0):
        b.append(val[i])
    else:
        c.append(val[i])
for j in b:
    d=sum(b)
for k in c:
    f=sum(c)
if(d>f):
    print(d)
else:
    print(f)
