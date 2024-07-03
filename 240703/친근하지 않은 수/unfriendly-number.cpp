#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,count = 0;
    cin >> n;
    for (int i = 1; i <=n; i++)
    {
        if(!(i % 2) || !(i%3) || !(i%5)) continue;
        count++;
    }
    cout << count;
    return 0;
}