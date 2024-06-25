#include <iostream>
using namespace std;
int main() {
    double ft_size = 30.48;
    int mi_size = 160934;
    cout << fixed;
    cout.precision(1);
    cout << "9.2ft" <<" = "<<ft_size * 9.2<<"cm"<<endl;
    cout << "1.3mi" <<" = "<< double(mi_size) * 1.3 <<"cm"<< endl;
    return 0;
}