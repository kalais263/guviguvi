C=int(input())
D=list(map(int,input().split()))
t=[]
while(len(D)!=0):
  if len(D)>1:
    t.append(max(D))
    t.append(min(D))
    D.remove(max(D))
    D.remove(min(D))
  else:
    t.append(max(D))
    D.remove(max(D))
print(*t,end="")  
