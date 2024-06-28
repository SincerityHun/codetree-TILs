#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> a >> b;
    for (;a<=b;a++) if(a%2!=0) cout << a << " ";
    return 0;
}