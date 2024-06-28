#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    cout << (((n % 2 != 0 && n % 3 == 0) || (n%2 == 0 && n%5 == 0)) ? "true" : "false");
    return 0;
}