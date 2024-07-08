#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    double arr[5],cnt = 0;
    cin >> n;
    for(int i = 0 ; i < n; i++)
    {
        cin >> arr[i];
    }
    for(int i = 0 ; i <n; i++) 
    {
        cnt += arr[i];
    }
    cout << fixed;
    cout.precision(1);
    cout << cnt/n << endl;
    if(cnt/n >= 4.0) cout <<"Perfect";
    else if(cnt/n >= 3.0) cout << "Good";
    else cout <<"Poor";

    return 0;
}