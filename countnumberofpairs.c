#include<stdio.h>
#include<conio.h>
int a[100],i,c=0,j,n;
int main()
{
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]<a[j])
{
c=c+1
}
}
}
printf("%d",c);
return 0;
}
