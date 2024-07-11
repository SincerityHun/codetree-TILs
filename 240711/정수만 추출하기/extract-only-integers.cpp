#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a,b;
    string a_next, b_next;
    cin >> a >> b;
    for(int i = 0 ; i < a.length(); i++) if(isdigit(a[i])) a_next += a[i]; else break;
    for(int i = 0 ; i < b.length(); i++) if(isdigit(b[i])) b_next += b[i]; else break;
    cout << stoi(a_next) + stoi(b_next) ;
    return 0;
}