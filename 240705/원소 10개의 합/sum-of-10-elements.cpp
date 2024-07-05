#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    for(int i = 0 ; i < 10; i++) cin >> arr[i];
    for(int i = 1; i <10; i++) arr[0] += arr[i];
    cout << arr[0];
    return 0;
}