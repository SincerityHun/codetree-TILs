#include <iostream>
#include <string>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    string var1;
    cin >> var1;
    char item;
    cin >> item;
    int index = var1.find(item);
    if(index != string::npos) cout << index;
    else cout << "No";
    return 0;
}