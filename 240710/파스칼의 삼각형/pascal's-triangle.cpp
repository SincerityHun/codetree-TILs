#include <iostream>
using namespace std;
bool in_range(int r,int c)
{
    return 0<=r && 0<=c && r >= c;
}
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int arr[15][15];
    int cur_r = 0, cur_c = 0;
    while(cur_r < n)
    {
        //value 구하기
        int prev1_r = cur_r -1, prev1_c = cur_c - 1,prev1_value = 0;
        int prev2_r = cur_r -1, prev2_c = cur_c,prev2_value = 0;
        if(in_range(prev1_r, prev1_c)) prev1_value = arr[prev1_r][prev1_c];
        if(in_range(prev2_r, prev2_c)) prev2_value = arr[prev2_r][prev2_c];
        int value = ((prev1_value == 0 && prev2_value == 0) ? 1 : prev1_value + prev2_value); 
        //값 넣기
        arr[cur_r][cur_c] = value;
        //r 업데이트하기
        if(cur_r > cur_c) cur_c++;
        else{
            cur_r++;
            cur_c = 0;
        }
    }
    for(int i = 0 ; i < n; i++)
    {
        for(int j = 0; j <= i; j++)
        {
            cout << arr[i][j] <<" ";
        }
        cout << endl;
    }
    return 0;
}