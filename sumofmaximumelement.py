a=int(input())
b=list(map(int,input().split()))[:a]
b.pop(0)
print(sum(b))
