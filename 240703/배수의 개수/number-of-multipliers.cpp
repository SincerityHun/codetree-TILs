#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int temp,count1 = 0,count2 = 0;
    for(int i = 0 ; i < 10;i++)
    {
        cin >> temp;
        (temp %3 == 0) ? count1++ : 0;
        (temp %5 == 0) ? count2++ : 0;
    }
    cout << count1 <<" "<<count2;
    return 0;
}