#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,yoon = 0;
    cin >> n;
    for(int i = 1; i <= n;i++)
    {
        if(!(i%4))
        {
            if(i%100 == 0 && i %400 != 0) continue;
            yoon++;
        }
    }
    cout << yoon << endl;
    return 0;
}