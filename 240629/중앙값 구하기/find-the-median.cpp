#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    cin >>a>>b>>c;
    cout << (a > b ? (b>c?b:(c>a?a:c)):(a>c?a:(c>b?b:c)));
    return 0;
}