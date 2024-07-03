#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n, sum_val = 0,i = 1;
    cin >> n;
    for(; i<=100 && sum_val < n;i++)
    {
        sum_val += i;
    }
    cout << (i-1);

    return 0;
}