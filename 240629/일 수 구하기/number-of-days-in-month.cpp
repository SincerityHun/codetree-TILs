#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    if(n == 2) {cout << 28 << endl;return 0;}
    if (n%2 == 0) cout <<(n<8 ? 30 : 31) <<endl;
    else cout << (n<8 ? 31:30)<<endl;
    
    return 0;
}