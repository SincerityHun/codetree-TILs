#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> b >> a;
    while(b >= a)
    {
        cout << b << " ";
        b -= 2;
    }
    return 0;
}