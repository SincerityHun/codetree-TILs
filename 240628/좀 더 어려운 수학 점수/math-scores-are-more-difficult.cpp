#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a_math, a_eng, b_math, b_eng;
    cin >> a_math >> a_eng >> b_math >> b_eng;
    if(a_math != b_math)
    {
        cout << (a_math > b_math ? "A" : "B")<<endl;
    }
    else
    {
        cout << (a_eng > b_eng ? "A" : "B") << endl;
    }
    return 0;
}