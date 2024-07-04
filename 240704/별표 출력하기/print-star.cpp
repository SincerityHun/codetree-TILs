#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 0 ; i < n-1; i++ )
    {
        for(int j = 0 ; j <= i ; j++) cout << "* ";
        cout << endl;
    }
    for(int i = 0; i < n; i++) cout <<"* ";
    cout <<endl;
    for(int i = 0; i<n-1;i++)
    {
        for(int j = n-1;j>i;j-- ) cout <<"* ";
        cout <<endl;
    }
    return 0;
}