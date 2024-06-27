#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int h, w;
    cin >> h >> w;
    int  b = (10000*w)/(h * h);
    cout << fixed;
    cout << b << endl;
    if (b >= 25) cout << "Obesity" << endl;
    return 0;
}