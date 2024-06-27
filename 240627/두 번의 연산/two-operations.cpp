#include <iostream>
using namespace std;
int main() {
    int a;
    cin >> a;
    a = (a%2!=0 ? a+3 : a);
    a = (a%3 == 0 ? a /3 : a);
    cout << a;
    return 0;
}