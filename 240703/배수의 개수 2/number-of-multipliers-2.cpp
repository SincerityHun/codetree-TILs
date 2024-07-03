#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int temp, count = 0;
    for(int i = 0; i < 10; i++)
    {
        cin >> temp;
        (temp % 2) ? count ++ : 0;
    }
    cout << count;
    return 0;
}