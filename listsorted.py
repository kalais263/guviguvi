a=int(input())
b=input().split()
t=[]
for i in sorted(b):
  t.append(i)
if(t==b):
  print("yes")
else:
  print("no")
