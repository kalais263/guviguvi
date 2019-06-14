a=input()
t=[]
for i in a:
  t.append(i)
for i in sorted(t):
  print(*i,end="")
