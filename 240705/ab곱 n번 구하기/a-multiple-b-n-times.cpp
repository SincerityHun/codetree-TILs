#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,a,b;
    cin >> n;
    for(int i = 0 ; i < n; i++)
    {
        cin >> a >> b;
        for(int j = a+1 ; j<=b; j++) a *= j;
        cout << a << endl;
    }
    return 0;
}