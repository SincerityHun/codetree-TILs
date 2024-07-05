#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    char arr[10];
    for(int i = 0 ; i<10; i++) cin >> arr[i];
    for(int i = 0 ; i < 10; i++) cout <<  arr[9-i];
    return 0;
}