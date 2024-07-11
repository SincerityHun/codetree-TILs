#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string A,B;
    cin >> A >> B;
    int index = A.find(B);
    while(index != string::npos)
    {
        A.erase(index, B.length());
        index = A.find(B);
    }
    cout << A;
    return 0;
}