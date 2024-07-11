#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,result = 0;
    cin >> a >> b;
    a += b;
    string str_a = to_string(a);
    for(int i = 0 ; i < str_a.length();i++)
    {
        if(str_a[i] == '1') result ++;
    }
    cout << result;
    return 0;
}