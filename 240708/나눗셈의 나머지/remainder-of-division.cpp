#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    int arr[10] = {}; // 0~9까지 몇번?
    cin >> a >> b;    
    while(a>1)
    {
        int remainder = a % b;
        arr[remainder] ++;
        a /= b;
    }
    int result = 0;
    for(int i = 0; i < 10; i++) result += arr[i] * arr[i];
    cout << result;
    return 0;
}