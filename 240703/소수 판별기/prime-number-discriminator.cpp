#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,i;
    cin >> n;
    for(i = 2;i<n && n%i!=0;i++);
    if(i<n) cout <<"C";
    else cout <<"P";
    return 0;
}