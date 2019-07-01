n=input()
s="dhoni"
c=0
if(len(n)==5):
    for i in range(0,len(s)):
        if(n[i] in s):
            c=c+1
    if(c==5):
        print("yes")
    else:
        print("no")
else:
    print("no")
