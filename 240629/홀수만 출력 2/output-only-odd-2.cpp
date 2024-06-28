#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> b >> a;
    for (;b>=a;b--)if(b%2!=0) cout << b << " ";
    return 0;
}