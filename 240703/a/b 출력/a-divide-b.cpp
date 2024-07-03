#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,count=20;
    cin >> a >> b;
    cout << a/b <<".";
    while(count-- > 0)
    {
        a *= 10;
        cout << a/b%10;
        a %= b;

    }
    return 0;
}