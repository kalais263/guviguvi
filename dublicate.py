def remove(d):
  b=[]
  for i in d:
    if i not in b:
      b.append(i)
  return b
a=input()
d=[]
for i in a:
  d.append(i)
print(*remove(d),sep="")
