a=input()
t=[]
for i in a:
  if i not in t:
    t.append(i)
t.sort()
print(*t[::-1],sep="")
