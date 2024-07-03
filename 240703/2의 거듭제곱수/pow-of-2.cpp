#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int N,i = 1,temp = 2;
    cin >> N;
    for(; i <= 10 && temp != N ; temp*=i,i++)
    {
    }
    cout << (i-1) ;
    return 0;
}