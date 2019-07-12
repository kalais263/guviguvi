t=[]
def func(a):
  if(a>1):
    func(a//2)
  n=a%2
  t.append(n)
a=int(input())
func(a)
print(len(t))
