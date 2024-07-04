#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 1; i < n+1;i ++)
    {
        for(int j = 1; j<n+1; j++) {cout << i << " * " << j << " = " << i*j; if(j == n) break; cout<<", ";}
        cout << endl;
    }
    return 0;
}