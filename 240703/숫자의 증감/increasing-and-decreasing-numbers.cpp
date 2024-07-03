#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    char c;
    int n;
    cin >> c >> n;
    if(c == 'A')
    {
        for(int i = 1; i <=n;i++) cout << i << " ";
    }
    else
    {
        while(n-->0)cout<<n+1<<" ";
    }
    return 0;
}