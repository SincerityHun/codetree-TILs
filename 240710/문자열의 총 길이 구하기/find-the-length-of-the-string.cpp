#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[10];
    int count = 0;
    for(string item:arr)
    {
        cin >> item;
        count += item.length();
    }
    cout << count ;
    return 0;
}