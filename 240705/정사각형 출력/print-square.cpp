#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,cnt=1;
    cin >> n;
    for(int i = 0; i < n ; i++) {for(int j = 0; j < n;j++,cnt++) cout << cnt<<" "; cout<<endl;}

    return 0;
}