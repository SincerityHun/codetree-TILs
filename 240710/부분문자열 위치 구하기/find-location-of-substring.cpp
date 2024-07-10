#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string first;
    string second;
    cin >> first;
    cin >> second;
    int index = first.find(second);
    if(index != string::npos) cout << index;
    else cout << -1;
    return 0;
}