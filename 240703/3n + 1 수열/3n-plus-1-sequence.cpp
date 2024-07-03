#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int N,count = 0;
    cin >> N;
    while(true)
    {
        if(N == 1) break;
        if(N%2 == 0) N /= 2;
        else N = (N*3) + 1;
        count++;
    }
    cout << count;
    return 0;
}