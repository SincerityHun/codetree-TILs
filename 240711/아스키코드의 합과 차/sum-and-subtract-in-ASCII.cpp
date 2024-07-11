#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char a,b;
    cin >> a >> b;
    cout << (int)a + (int)b <<" "<<((a > b)?(int)a - (int)b:(int)b - (int)a);
    return 0;
}