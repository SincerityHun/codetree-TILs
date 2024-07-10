#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string var1;
    cin >> var1;

    if(var1.find("ee") != string::npos) cout <<"Yes ";
    else cout <<"No ";
    if(var1.find("ab") != string::npos) cout <<"Yes ";
    else cout <<"No ";
    return 0;
}