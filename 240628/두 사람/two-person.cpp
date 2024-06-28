#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a_age, b_age;
    char a_sex, b_sex;
    cin >> a_age >> a_sex >> b_age >> b_sex;

    cout << ((a_age >= 19 && a_sex == 'M') || (b_age >= 19 && b_sex == 'M')) << endl;
    return 0;
}