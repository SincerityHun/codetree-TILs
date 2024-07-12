#include <iostream>
#include <deque>
#include <climits>
using namespace std;

bool in_arr(int i, int j, int N)
{
    return 0<= i && i < N && 0 <= j && j < N;
}
int count_coin(int i, int j, deque<deque<int>>& arr,int N)
{
    int result = 0;
    for(int r = 0; r < 3; r++)
    {
        for(int c = 0; c < 3; c++)
        {
            if(!in_arr(i+r,j+c,N)) return -1;
            result += arr[i+r][j+c];
        }

    }
    return result;
}
int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    int max_num = INT_MIN;
    cin >> N;
    deque<deque<int>> arr(N, deque<int>(N));
    for(int i =0 ; i < N; i++)
    {
        for(int j = 0 ; j < N; j++)
        {
            cin >> arr[i][j];
        }
    }
    for(int i = 0 ; i < N-2;i++)
    {
        for(int j = 0 ; j < N-2; j++)
        {
            int temp_re = count_coin(i,j,arr,N);
            if(temp_re > max_num) max_num = temp_re;
        }
    }
    cout << max_num;

    return 0;
}