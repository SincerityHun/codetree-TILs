#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n,cnt1= 1, cnt2 = 0;
    cin >> n;
    cnt2 = n;
    for(int i = 1; i < 2*n+1; i++)
    {
        if(i%2 != 0) for(int j = 0 ; j< cnt1;j++) cout << "* "; // 홀
        else for(int j = 0; j< cnt2 ; j++) cout <<"* "; // 짝
        cout << endl;
        if(i == n-1) continue;
        if(i == n){int temp = cnt1;cnt1 = cnt2;cnt2=temp;continue;}
        
        if(i%2 != 0) cnt1++;
        else cnt2--;

    }    
    
    return 0;
}