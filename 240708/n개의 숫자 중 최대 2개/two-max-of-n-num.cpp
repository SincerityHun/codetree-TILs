#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    cin >> N;
    // int arr[100];
    int Best = INT_MIN, Next = INT_MIN;
    for(int i = 0 ; i < N ; i++)
    {
        int x;
        cin >> x;
        // best 보다 커?
        if(Best <= x) {
            Next = Best;
            Best = x;
        }
        else if(Next <= x) Next = x;
    }
    cout << Best << " " << Next;
    return 0;
}