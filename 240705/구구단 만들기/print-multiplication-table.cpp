#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    for(int i = 1; i < 10; i++)
    {
        for(int j = b; j>=a; j-= 2 )
        {
            cout<<j<<" * "<<i<<" = "<<i*j;
            if(j == a) break;
            cout << " / ";
        }
        cout << endl;
    }
    return 0;
}