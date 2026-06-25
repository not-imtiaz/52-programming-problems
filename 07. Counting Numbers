#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
    int i, j, n;
    cin >> n;
	
    for(i = 0; i < n; i++)
    {
        int cnt = 1;
        string num;
        cin.ignore();
        getline(cin, num);
		
        for(j = 0; num[j] != '\0'; j++)
            if(num[j] == ' ' && num[j+1] != ' ')
                cnt++;

        cout << cnt << endl;
    }
	
    return 0;
}
