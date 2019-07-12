a,b,c=list(map(str,input().split()))
t=[]
for i in a:
  t.append(i)
for i in t:
  if(t.index(i)==int(b)):
    print(i)
