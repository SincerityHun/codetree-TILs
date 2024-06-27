#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    char temp;
    cin >> temp;
    if (temp == 'S') cout << "Superior" ;
    else if (temp == 'A') cout << "Excellent" ;
    else if (temp == 'B') cout << "Good" ;
    else if (temp == 'C') cout << "Usually" ;
    else if (temp == 'D') cout << "Effort" ;
    else cout << "Failure" ;
    return 0;
}