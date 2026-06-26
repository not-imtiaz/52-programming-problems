#include <iostream>

using namespace std;

int main()
{
	int i, j, t, num, div;
    cin >> t;
		
    for(i = 0; i<t; i++)
    {
    	cin >> num;
        cout << "Case " << i+1 << ": ";
        
        for(j = num; j > 0; j--)
        {
			if(num % j == 0)
                cout << num/j;
            if(j == 1)
                cout << endl;
            else if(num % j == 0 && j != 0)
                cout << " ";
        }
    }
	
	return 0;
}

