a,b=input().split()
t=[]
for i in a:
  t.append(i)
a=len(a)
for i in range(1,a):
  if b in t:
    print(t.index(b)+1)
    break
