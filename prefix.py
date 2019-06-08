a=int(input())
t=[]
c=[]
for i in range(0,a):
  b=input()
  t.append(b)
for i in zip(*t):
  if i.count(i[0])==len(i):
    c.append(i[0])
  else:
    break
print(*c,sep="")
