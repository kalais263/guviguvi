n=int(input())
a=list(map(int,input().split()))[:n]
b=min(a)
c=max(a)
b=a.index(b)+1
c=a.index(c)+1
print(b,c)
