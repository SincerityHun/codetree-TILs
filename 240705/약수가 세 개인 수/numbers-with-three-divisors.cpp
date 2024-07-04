#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int start, end,count = 0;
    cin >> start >> end;
    for(;start<=end;start++)
    {
        int cnt = 0;
        for(int i = 1; i <= start/2; i++) if(start % i == 0) cnt++;
        if(cnt == 2) count ++;
    }
    cout << count;
    return 0;
}