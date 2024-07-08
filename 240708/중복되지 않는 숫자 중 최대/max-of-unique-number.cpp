#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    int arr[1000];
    int visited[1000] = {};
    cin >> N;
    for(int i = 0 ; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;
        visited[temp]++;
    }
    int Best = INT_MIN; 
    for(int i = 0 ; i < N;i++)
    {
        if(Best <= arr[i] && visited[arr[i]] == 1) Best = arr[i];
    }
    if(Best == INT_MIN) cout<< -1;
    else cout << Best;
    return 0;
}