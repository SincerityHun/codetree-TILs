#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,limit_count;
    cin >> n;
    for(int i = 0; i < n; i++) cout<<"* ";
    cout << endl;
    if(n == 1) return 0;
    if(n == 2)
    {
       for(int i = 0; i < n; i++) cout<<"* ";
       cout << endl; 
       return 0;
    }
    limit_count = 1;
    for(int i = 0; i < n-2 ; i++)
    {
        for(int j = 0; j < limit_count ; j++) cout <<"* ";
        for(int j = 0; j < n-limit_count-1 ; j++) cout <<"  ";
        cout << "* " << endl;
        limit_count++;

    }
    for(int i = 0; i < n; i++) cout<<"* ";

    return 0;
}