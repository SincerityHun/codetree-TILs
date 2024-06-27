#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a_math,a_eng, b_math, b_eng;
    cin >> a_math >> a_eng >> b_math >> b_eng;
    cout << (a_math > b_math && a_eng > b_eng) <<endl;
    return 0;
}