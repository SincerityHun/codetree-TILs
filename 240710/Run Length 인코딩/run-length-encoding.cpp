#include <iostream>
#include <string>
using namespace std;
int count_digit(int n)
{
    int count = 0;
    while(n>0)
    {
        n /= 10;
        count ++;
    }
    return count;
}
int main() {
    // 여기에 코드를 작성해주세요.
    string A;
    cin >> A;
    char cur_item = A[0];
    int arr[1000] = {},cnt = 0; //index,count
    for(int i = 0 ; i < A.length(); i++)
    {
        // 현재꺼 가져오기
        if(A[i] == cur_item) arr[cnt+1]++;
        // 가져왔는데 같은 경우
            // cnt+1 에 ++
        else{
            cur_item = A[i];
            cnt += 2;
            arr[cnt] = i;
            arr[cnt+1]++;
        }
        // 가져왔는데 다른 경우
            // cur_item 업데이트
            // cnt 업데이트
    }
    int result = 0;
    for(int i = 0 ; i <= cnt; i+=2)
    {
        result++;
        result += count_digit(arr[i+1]);
    }
    cout << result << endl;
    for(int i = 0 ; i <= cnt; i+=2)
    {
        cout << A[arr[i]]<<arr[i+1];
    }
    return 0;
}