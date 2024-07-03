#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,clean2 = 0, clean3 = 0, clean12 = 0;
    cin >> n;
    for (int i = 1 ; i <= n; i ++)
    {
        if(i % 12 == 0) clean12++;
        else if(i % 3 == 0) clean3++;
        else if(!(i%2)) clean2++;
    }
    cout << clean2 <<" " << clean3 << " " << clean12;
    return 0;
}