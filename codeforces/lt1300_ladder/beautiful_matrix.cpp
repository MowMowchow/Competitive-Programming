#include <bits/stdc++.h>
using namespace std;
int temp, res = 0;
int main(){
    for (int i = 1; i <= 5; i++){
        for (int j = 1; j <= 5; j++){
            cin >> temp;
            if (temp == 1){
                res = abs(3-i)+abs(3-j);
            }
        }
    }
    cout << res;
    return 0;
}