#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[4] = {}; // A B C D
    for(int i = 0 ; i < 3; i++)
    {
        char sym;
        int degree;
        cin >> sym;
        cin >> degree;
        if(sym == 'Y')
        {
            if(degree >= 37) arr[0] += 1;
            else arr[2] += 1;
        }
        else{
            if(degree >= 37) arr[1]+= 1;
            else arr[3] += 1;
        }
    }
    for(int i = 0; i < 4; i++) cout << arr[i] << " ";
    if(arr[0] >= 2) cout <<"E";
    return 0;
}