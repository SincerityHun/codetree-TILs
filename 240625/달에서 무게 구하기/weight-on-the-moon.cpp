#include <iostream>
using namespace std;
int main() {
    int weight = 13;
    double ratio = 0.165;
    cout << fixed;
    cout.precision(6);

    cout << weight <<" * "<<ratio <<" = "<< weight * ratio << endl;
    return 0;
}