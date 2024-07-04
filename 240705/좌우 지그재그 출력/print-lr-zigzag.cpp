#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,cnt=1;
    cin >> n;
    for(int i = 1; i < n+1; i++)
    {
        for(int j = 1; j < n+1; j++)
        {
            if(i%2!=0) cout << cnt++ <<" ";
            else cout << cnt-- << " ";
        }
        if(i%2!=0) cnt += (n-1);
        else cnt += (n+1);
        cout << endl;
    }
    return 0;
}