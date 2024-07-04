#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,limit_start = 1;
    cin >> n;
    for(int i = 1 ; i < n+1; i++)
    {
        for(int j = 1 ; j < n+1; j++)
        {
            if(j<limit_start) cout <<"  ";
            else if( i == 1) cout <<"* ";
            else if(j%2!=0) cout <<"  ";
            else cout <<"* ";
        }
        cout << endl;
        limit_start++;
    }
    return 0;
}