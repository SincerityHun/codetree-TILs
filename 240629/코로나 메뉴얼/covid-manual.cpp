#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    char a_sym, b_sym, c_sym;
    int a_value, b_value, c_value;
    cin >> a_sym>>a_value >> b_sym >> b_value >> c_sym >> c_value;
    int count = 0;
    if(a_sym == 'Y' && a_value >= 37) count += 1;
    if(b_sym == 'Y' && b_value >= 37) count += 1;
    if(c_sym == 'Y' && c_value >= 37) count += 1;
    if(count >= 2) cout<<"E"<<endl;
    else cout <<"N"<<endl;
    return 0;
}