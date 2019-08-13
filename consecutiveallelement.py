a=int(input())
b=list(map(int,input().split()))[:a]
b.remove(b[0])
print(sum(b))
