#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[2][4];
    for(int i = 0 ; i < 2;i++)
    {
        for(int j = 0 ; j < 4; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << fixed;
    cout.precision(1);
    int total_sum = 0;
    for(int i = 0 ; i < 2; i++)
    {
        int temp_sum = 0;
        for(int j = 0 ; j < 4; j++) temp_sum += arr[i][j];
        cout << (double)temp_sum / 4 << " ";
        total_sum += temp_sum;
    }
    cout << endl;
    for(int j = 0 ; j < 4; j++)
    {
        int temp_sum = 0;
        for(int i = 0; i< 2 ; i++) temp_sum += arr[i][j];
        cout << (double) temp_sum / 2 << " ";
    }
    cout << endl;
    cout << (double) total_sum / 8 ;
    return 0;
}