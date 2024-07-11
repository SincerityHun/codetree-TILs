#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string item;
    cin >> item;
    string result;
    for(int i = 0 ; i < item.length(); i++)
    {
        if(isalpha(item[i])) result += toupper(item[i]);
    }
    cout << result;
    return 0;
}