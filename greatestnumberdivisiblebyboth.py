def hcf(a,b):
  if(b==0):
    return a
  else:
    return hcf(b,a%b)
a,b=list(map(int,input().split()))
print(int(hcf(a,b)))
