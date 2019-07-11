a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
for i in range(0,a):
  for j in range(1,a-1):
    c=abs(b[i]-b[j])
t.append(c)
print(min(t))
