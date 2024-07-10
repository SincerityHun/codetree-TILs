#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int arr[1000],cnt = 0; // 변곡점 저장
    int prev_value = INT_MAX;
    bool falling = true; // 내리는 중이라고 가정
    
    for(int i = 0 ; i < n ; i++)
    {
        int cur_value;
        cin >> cur_value;
        //극점 확인
        if((falling && cur_value > prev_value) || (!falling && cur_value < prev_value))
        {
            arr[cnt++] = prev_value;
            // cout << arr[cnt-1] << endl;
        }
        if(i == n-1) arr[cnt++] = cur_value;
        //falling 업데이트
        if(prev_value < cur_value) falling = false;
        else falling = true;
        //prev_value 업데이트
        prev_value = cur_value;
    }
    int max_value = INT_MIN;
    for(int i = 0 ; i < cnt; i++)
    {
        for(int j = i+1; j< cnt; j++)
        {
            if(max_value < arr[j] - arr[i]) max_value = arr[j] - arr[i];
        }
    }
    if(max_value < 0) max_value = 0;
    cout << max_value;

    return 0;
}