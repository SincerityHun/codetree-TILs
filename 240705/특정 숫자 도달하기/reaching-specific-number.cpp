#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10], sum_val = 0,i;
    for(i = 0 ; i < 10; i++) {
        cin >> arr[i];
        if(arr[i]>=250) break;
        sum_val += arr[i];
        
        }
    cout << fixed;
    cout.precision(1);
    cout << sum_val <<" "<< (double) sum_val / i;
    return 0;
}