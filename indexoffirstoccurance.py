a=input()
b=input()
t=[]
n=[]
for i in a:
  t.append(i)
for i in t:
  for j in b:
    if(i==j):
      n.append(t.index(i))
      break
    break
print(n[0])
