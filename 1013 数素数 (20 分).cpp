#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int i,j;
    int M,N;
    int count=0;
    int showNUM=0;
    cin>>M>>N;
    for(i=2;i<=104730;i++)
    {
        for(j=2;j<=sqrt(i);j++)
        {
            if(i%j==0)
                break;
        }
        if(j>sqrt(i))
        {
            count++;
            if (count>N)
                break;
            if(count>=M)
            {
                showNUM++;
                if(showNUM%10==0 || count==N)
                    cout<<i<<endl;
                else
                    cout<<i<<" ";
            }
        }
        
    }
}   
