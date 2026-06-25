#include<cstring>
#include<iostream>

using namespace std;

int main()
{
    int i, n, first, last;
    cin >> n;
    
    for(i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        
        first = num % 10;
        while(num >= 10)
        {
            num = num/10;
        }
        
        last = num;
        cout << "Sum = " << first + last << endl;
    }
    
    return 0;
}
