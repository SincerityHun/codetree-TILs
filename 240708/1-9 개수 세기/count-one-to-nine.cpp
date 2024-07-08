#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt_arr[10] = {};
    for(int i = 0 ; i < n; i++)
    {
        int temp;
        cin >> temp;
        cnt_arr[temp] ++;
    }
    for(int i = 1 ; i <10; i++)
    {
        cout << cnt_arr[i] << endl;
    }
    return 0;
}