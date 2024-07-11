#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[5];
    for(int i = 0 ; i <5;i++) cin >> arr[i];
    for(int i = 0 ; i < 5; i++) cout << (char)arr[i] <<" ";
    return 0;
}