a=input()
t=[]
for i in a:
  if(int(i)%2==1):
    t.append(i)
b=sum(t)
if(b%2==0):
  print("E")
else:
  print("O")
