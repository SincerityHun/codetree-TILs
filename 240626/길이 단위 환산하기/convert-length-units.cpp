#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    double ft;
    cin >> ft;
    cout << fixed;
    cout.precision(1);
    cout << ft * 30.48 << endl;
    return 0;
}