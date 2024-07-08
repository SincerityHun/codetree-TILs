#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,q, arr[100];
    cin >> n >> q;
    for(int i = 0 ; i < n; i++) cin >> arr[i];
    for(int i = 0 ; i < q; i ++)
    {
        int kind,x,y;
        cin >> kind;
        if(kind == 1)
        {
            cin >> x;
            cout << arr[x-1] << endl;
        }
        else if(kind == 2)
        {
            cin >> x;
            int j = 0 ;
            for(; j < n; j++)
            {
                if(arr[j] == x) break;
            }
            if(j!=n) cout << j+1 << endl;
            else cout << 0 << endl;
        }
        else{
            cin >> x;
            cin >> y;
            for(;y>=x; x++)
            {
                cout << arr[x-1] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}