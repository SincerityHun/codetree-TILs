#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,i = 2;
    cin >> n;
    for(; i<n && n%i !=0;i++);
    if(i == n) cout <<"N";
    else cout << "C";
    return 0;
}