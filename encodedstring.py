a=input()
b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t=[]
for i in a:
  n=b.index(i)
  e=n+3
  if(e<=25):
    p=b[e]
    t.append(p)
  elif(e>25):
    p=e%26
    s=b[p]
    t.append(s)
print(*t,sep="")
