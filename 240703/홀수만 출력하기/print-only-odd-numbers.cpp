#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int N,temp;
    cin >> N;
    while(N-->0)
    {
        cin >> temp;
        if((temp % 2) && (temp % 3 == 0)) cout << temp <<endl;
    }
    return 0;
}