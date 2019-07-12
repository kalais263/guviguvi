n=int(input())
a=list(map(int,input().split()))[:n]
b=set(a)
print(*b,end="")
