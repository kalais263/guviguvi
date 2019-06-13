def func(a,b,c):
  d=a*b
  print(d%c)
a,b,c=list(map(int,input().split()))
func(a,b,c)
