#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 1; i < n+1;i++)
    {
        for(int j = 1; j < n+1; j++)
        {
            if(j%2!=0) cout << i;
            else cout << n+1-i;
        }
        cout << endl;
    }
    return 0;
}