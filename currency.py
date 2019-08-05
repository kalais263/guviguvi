t=[]
def currency(a):
  n=[1000,500,100,50,10,1]
  n1=[0,0,0,0,0,0]
  for i,j in zip(n,n1):
    if(a>=i):
      j=a//i
      a=a-j*i
      t.append(j)
a=int(input())
currency(a)
print(sum(t))
