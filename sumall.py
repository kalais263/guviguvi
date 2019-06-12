a=int(input())
b=list(map(int,input().split()))
sum=0
t=[]
for i in b:
  t.append(i)
for i in t:
  sum=sum+i
print(sum)
