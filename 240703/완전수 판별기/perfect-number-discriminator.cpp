#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,sum_val = 0;
    cin >> n;
    for(int i = 1; (i*2) <= n; i++)
    {
        if(n%i == 0) sum_val += i;
    }
    cout << (sum_val == n ? "P" : "N") << endl;
    return 0;
}