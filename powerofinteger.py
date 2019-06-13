a=input()
sum=0
b=0
t=[]
for i in a:
  t.append(i)
for i in t:
  d=int(i)
  sum=sum+(d**b)
  b=b+1
print(sum)
