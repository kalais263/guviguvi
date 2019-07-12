def binary(a):
  if(a>1):
    binary(a//2)
  print(a%2,end="")
a=int(input())
binary(a)
