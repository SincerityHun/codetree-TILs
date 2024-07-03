#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,count = 0;
    for(int i = 0 ; i<5; i++)
    {
        cin >> n;
        n % 2 == 0 ? count++ : 0;
    }
    cout <<count ;
    return 0;
}