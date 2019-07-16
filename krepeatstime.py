a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
n=0
t=[]
for i in c:
  if(i==b):
    t.append(i)
if(len(t)>0):
  print("yes",len(t))
else:
  print("no")
