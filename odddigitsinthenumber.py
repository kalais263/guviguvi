a=input()
t=[]
n=0
for i in a:
  if(int(i)%2==1):
    t.append(i)
for i in t:
  n=n+i
if(n%2==0):
  print("E")
else:
  print("O")
