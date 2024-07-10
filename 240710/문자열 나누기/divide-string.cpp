#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    string arr,total;
    for(int i = 0 ; i < n; i++) {cin >> arr; total += arr;}
    for(int i = 0 ; i < total.length(); i++)
    {
        cout << total[i];
        if((i+1)%5 == 0) cout << endl;
    }
    
    return 0;
}