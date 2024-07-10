#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[10];
    char test_case;
    bool flag = true;
    for(int i = 0 ; i < 10; i++)
    {
        cin >> arr[i];
    }
    cin >> test_case;
    for(string item: arr)
    {
        if(test_case == item[item.length()-1]) {cout << item << endl; flag = false;}
    }
    if(flag) cout <<"None";
    return 0;
}