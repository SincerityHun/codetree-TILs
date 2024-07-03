#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> a >> b;
    while(b>=a)
    {
        cout << a << " ";
        (a%2) ? (a*=2) : (a+=3);
    }
    return 0;
}