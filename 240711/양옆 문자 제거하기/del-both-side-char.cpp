#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string item;
    cin >> item;
    item = item.substr(0,1) + item.substr(2,item.length()-4) + item.substr(item.length()-1,1);
    cout <<item;
    return 0;
}