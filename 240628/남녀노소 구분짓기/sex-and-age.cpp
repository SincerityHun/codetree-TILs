#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int sex, age;
    cin >> sex >> age;
    if (sex == 0 && age >=19) cout << "MAN";
    else if(sex == 0) cout << "BOY";
    else if(sex == 1 && age >= 19) cout <<"WOMAN";
    else cout << "GIRL";
    return 0;
}