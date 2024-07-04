#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 1 ; i < 2*n+2;i++)
    {
        if(i%2 != 0 ) for(int j = 0 ; j < 2*n+1;j++) cout << "* ";
        else for(int j = 0; j < n+1; j++)cout<<"*   ";
        cout << endl;
    }
    return 0;
}