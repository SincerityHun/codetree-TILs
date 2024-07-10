#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[100][100];
    int n,m;
    cin >> n >> m;
    int count = 0 ;
    for(int i = 0 ; i < m; i++)
    {
        if(i%2 == 0)
        {
            for(int j = 0 ; j < n; j++)
                    {
                        arr[j][i] = count++;
                    }
        }
        else
        {
            for(int j = 0 ; j < n; j++)
            {
                arr[n-j-1][i] = count++;
            }
        }
        
    }
    for(int i = 0 ; i < n; i ++)
    {
        for(int j = 0 ; j < m ; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}