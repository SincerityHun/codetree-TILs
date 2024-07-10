#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[4];
    for(int i = 0 ; i < 4; i++)
    {
        cin >> arr[i];
    }
    for(int i = 0 ; i < 4; i++)
    {
        cout << arr[3-i] << endl;
    }
    return 0;
}