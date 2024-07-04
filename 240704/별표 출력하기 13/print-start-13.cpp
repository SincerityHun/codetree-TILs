#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,cnt_odd = 0, cnt_even = 0;
    cin >> n;
    cnt_odd = n;
    cnt_even = 1;
    for(int i = 1; i < 2*n + 1; i++)
    {
        if(i%2 != 0) for(int j = 0 ; j < cnt_odd;j++) cout<<"* ";
        else for(int j = 0; j< cnt_even; j++) cout <<"* ";
        cout << endl;

        if(i == n-1) continue;
        if(i == n) {int temp = cnt_odd; cnt_odd = cnt_even; cnt_even = temp; continue;}

        if(i%2 != 0) cnt_odd--;
        else cnt_even++;
    }
    return 0;
}