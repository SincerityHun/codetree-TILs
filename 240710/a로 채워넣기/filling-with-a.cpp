#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string var;
    cin >> var;
    var[1] = 'a';
    var[var.length()-2] = 'a';
    cout << var;
    return 0;
}