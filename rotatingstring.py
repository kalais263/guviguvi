a,b=list(map(str,input().split()))
b=int(b)
n1=a[0:len(a)-b]
n2=a[len(a)-b:]
print(n2+n1)
