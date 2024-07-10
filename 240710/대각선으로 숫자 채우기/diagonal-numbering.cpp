#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;    
    cin >> n >> m;
    int count = 1;
    int arr[100][100];
    int i = 0, j = 0, limit = n+m-1; //5
    bool flag = false;
    while(i+j < limit)
    {
        //i,j에 넣어
        if(0<=i && i < n && 0<=j && j < m) arr[i][j] = count++;
        // 그다음 위치 찾아.
        i++;
        j--;
        if(j < 0)
        {
            j = (i+j+1);
            i = 0;
        }
    }
    for(int i =0 ; i < n; i++)
    {
        for(int j = 0 ; j < m; j++)
        {
            cout << arr[i][j] <<" ";
        }
        cout << endl;
    }
    return 0;
}