#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> a >> b;
    if(a>b) while(a-->=b) cout << a+1 << " ";
    else while(b-->=a) cout << b+1 << " ";
    return 0;
}