#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string s;
    int q;
    cin >> s;
    cin >> q;
    for(int i = 0 ; i < q; i++)
    {
        int type;
        cin >> type;
        if(type == 1)
        {
            int a,b;
            cin >> a >> b;
            char temp = s[a-1];
            s[a-1] = s[b-1];
            s[b-1] = temp;
        }
        else{
            char a,b;
            cin >> a >> b;
            int idx;
            while((idx = s.find(a))!= string::npos && a!=b)
            {
                s[idx] = b;
            }
        }
        cout << s << endl;
    }
    return 0;
}