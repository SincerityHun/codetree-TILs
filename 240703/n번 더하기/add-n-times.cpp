#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a,n,key;
    cin >> a >> n;
    key = n;
    while(n-- > 0 )
    {
        cout << (a+=key) << endl;
    }
    return 0;
}