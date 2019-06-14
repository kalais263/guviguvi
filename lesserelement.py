a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
t=[]
for i in sorted(c):
  t.append(i)
for i in t:
  if(i<b):
    print(i,end=" ")
