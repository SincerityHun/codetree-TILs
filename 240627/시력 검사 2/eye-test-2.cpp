#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    double aval;
    cin >> aval;
    if(aval >= 1) cout << "High" <<endl;
    else if(aval >= 0.5) cout << "Middle" << endl;
    else cout << "Low" ;
    return 0;
}