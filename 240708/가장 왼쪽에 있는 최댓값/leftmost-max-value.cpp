#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    int key[1000] = {}; // 변화점
    int key_index = 0;
    int max_value = INT_MIN;
    cin >> N;
    // for
    // 최댓값 -> key 에 넣고 + key index 증가
    for(int i = 1; i < N+1; i++)
    {
        int temp;
        cin >> temp;
        if(max_value < temp)
        {
            max_value = temp;
            key[key_index++] = i;
        }
    }
    for(int i = 0 ; i <key_index;i++)
    {
        cout << key[key_index - i - 1] << " ";
    }

    return 0;
}