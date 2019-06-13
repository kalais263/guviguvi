string=list(input())
l=len(string)-1
if l%2!=0:
    string[l//2]="*"
    string[l//2+1]="*"
else:
    string[l//2]="*"
print("".join(string))
