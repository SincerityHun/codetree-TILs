#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char test;
    int count = 0;
    cin >> test;
    for(string std : arr)
    {
        if(std[2] == test || std[3] == test)
        {
            cout << std << endl;
            count ++;
        }
    }
    cout << count ;
    return 0;
}