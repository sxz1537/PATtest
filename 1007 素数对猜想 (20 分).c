#include<stdio.h>
#include<math.h>
int main()
{
    int n,i,j;
    int temp=1;
    int count=0;
    scanf("%d",&n);
    for(i=2;i<=n;i++)
    {
        for(j=2;j<=sqrt(i);j++)
        {
            if(i%j==0)
                break;
        }
        if(j>sqrt(i))
        {
            if(i-temp==2)
            	count++;
            temp=i;
        }
    }
    printf("%d\n", count);
}
