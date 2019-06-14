a=int(input())
b=list(map(int,input().split()))
t=[]
for i in sorted(b):
  t.append(i)
for i in t:
  if(a>i):
    print(i,end=" ")
