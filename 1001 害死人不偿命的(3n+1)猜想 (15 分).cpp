#include <iostream>
using namespace std;
int main()
{
    int n=0;
    int x=0;
    cin>>x;
    while (x!=1)
        if (x%2==0)
        {
            x=x/2;
            n++;
        }
        else
        {
            x=(x*3+1)/2;
            n++;
        }
    cout<<n;
    return 0;
}