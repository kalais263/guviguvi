a=int(input())
sum=0
for i in str(a):
  sum=sum+int(i)
  b=str(sum)
if(str(sum)==b[::-1]):
  print("yes")
else:
  print("no")
