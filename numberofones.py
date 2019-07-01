a,b=list(map(int,input().split()))
n=list(map(int,input().split()))[:a]
f=0
for i in n:
    if(f!=b):
        n.pop()
        f=f+1
print(*n,end=" ")
