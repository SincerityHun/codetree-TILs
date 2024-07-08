#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n1, n2;
    cin >> n1 >> n2;
    int arr1[100], arr2[100];
    for(int i = 0 ; i < n1; i++) cin >> arr1[i];
    for(int i = 0; i < n2; i++) cin >> arr2[i];
    int i = 0;
    for(; i < n1; i++) 
    {
        if(arr1[i] == arr2[0])
        {
            int j = 1;
            for(;j<n2 && i+j < n1;j++) if(arr1[i+j] != arr2[j]) break;
            if(j == n2){
                cout << "Yes";
                break;
            }
        }
    }
    if(i == n1) cout << "No";
    return 0;
}