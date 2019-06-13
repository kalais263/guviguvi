a=int(input())
b=list(map(int,input().split()))
t=[]
for i in b:
  t.append(i)
t.reverse()
print(*t,sep="->")
