#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, arr[4],cnt = 0;
    cin >> n;
    for(int i = 0 ; i <n; i++)
    {
        for(int j = 0; j < 4; j++) cin >> arr[j];
        for(int j = 1; j < 4 ;j++) arr[0] += arr[j];
        if((double)arr[0]/4 >= 60) {cout << "pass" << endl;cnt++;}
        else cout <<"fail" << endl;
    }
    cout << cnt;
    return 0;
}