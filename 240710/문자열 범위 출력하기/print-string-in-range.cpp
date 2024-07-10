#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string test;
    getline(cin, test);
    for(int i = 2; i < 10; i++) cout << test[i];
    return 0;
}