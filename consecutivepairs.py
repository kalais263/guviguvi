a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
for i in range(0,a-1):
  c=b[i]+b[i+1]
  t.append(c)
print(sum(t))
