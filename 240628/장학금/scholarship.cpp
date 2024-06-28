#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> a >> b;
    if (a < 90) {cout << 0 << endl; return 0;}
    if (b >= 95) cout << 100000 <<endl;
    else if(b >= 90) cout << 50000 <<endl;
    else cout << 0 <<endl;
    return 0;
}