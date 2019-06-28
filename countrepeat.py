a=input().split()
b=input()
t=[]
c=0
for i in a:
  t.append(i)
for i in t:
  if(i==b):
    c+=1
print(c)
