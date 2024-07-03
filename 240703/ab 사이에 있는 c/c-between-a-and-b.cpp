#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    cin >> a >> b >> c;
    for (;a<=b && a%c !=0;a++);
    if(a<=b) cout <<"YES";
    else cout <<"NO";

    return 0;
}