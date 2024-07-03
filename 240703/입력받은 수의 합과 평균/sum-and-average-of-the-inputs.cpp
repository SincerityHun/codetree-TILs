#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,sum_val = 0, temp;
    cin >> n;
    for(int i = 0 ; i< n; i++)
    {
        cin >> temp;
        sum_val += temp;
    }
    cout << fixed;
    cout.precision(1);
    cout << sum_val << " " << (double) sum_val / n << endl;

    return 0;
}