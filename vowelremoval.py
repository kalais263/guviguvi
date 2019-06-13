a=int(input())
b=str(input())
b=b[::-1]
for i in range(a):
  if(b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u' or b[i]=='A' or b[i]=='E' or b[i]=='I' or b[i]=='O' or b[i]=='U'):
    continue
  else:
    print(b[i],end="")
