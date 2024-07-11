#include <iostream>
#include <string> 
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string start_str;
    int q;
    cin >> start_str >> q;
    while(q--)
    {
        int choice;
        cin >> choice;
        if(choice == 1)
        {
            start_str = start_str.substr(1,start_str.length()-1) + start_str[0];
        }
        else if(choice == 2)
        {
            start_str = start_str[start_str.length()-1] + start_str.substr(0,start_str.length()-1);
        }
        else
        {
            string temp;
            for(int i = 0 ; i < start_str.length(); i++)
            {
                temp += start_str[start_str.length() - 1 - i];
            }
            start_str = temp;
        }
        cout << start_str << endl;
    }
    return 0;
}