#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,cnt=1;
    cin >> n;
    int arr[10][10];
    int dx[3] = {-1,0,1}; // 상, 좌, 하
    int dy[3] = {0,-1,0};
    int dir = 0;
    int x = (n-1), y = (n-1);
    while(cnt <= n * n)
    {
        //채워넣고
        arr[x][y] = cnt++;
        //방향찾고
        if(dir == 0 && x - 1 < 0) dir = 1;
        else if(dir == 1 && x-1 <0) dir = 2;
        else if(dir == 1 && x+1 >= n) dir = 0;
        else if(dir == 2 && x+1 >= n) dir = 1 ;
        //x,y 업데이트
        x += dx[dir];
        y += dy[dir];
    }
    for(int i = 0 ; i < n; i++)
    {
        for(int j = 0 ; j < n; j++) cout << arr[i][j] <<" ";
        cout << endl;
    }
    return 0;
}