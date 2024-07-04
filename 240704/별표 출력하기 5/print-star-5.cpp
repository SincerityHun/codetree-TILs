#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        for(int j = n; j > i; j--)
        {
            for(int k = n; k > i;k--) cout << "*";
            cout <<" ";
        }
        cout << endl;
    }
    return 0;
}