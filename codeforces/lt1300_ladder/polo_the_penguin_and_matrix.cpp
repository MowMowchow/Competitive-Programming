#include <bits/stdc++.h>
using namespace std;
int n, m, d, matrix[110][110], fin = 999999999;
// n vertical, m horizontal

int solve(int k){
    int temp = 0; int res;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            res = abs(k-matrix[i][j]);
            if (res%d != 0 && (res-d)%d != 0 && (res+d)%d != 0){
                return -1;
            } else {
                temp += res;
            }
        }
    }
    return temp/d;
}
 
 
int main(){
    cin >> n >> m >> d;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> matrix[i][j];
        }
    }
    
    int re;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
           re = solve(matrix[i][j]) ;
           if (re != -1){
               fin = min(fin, re);
           }
        }
    }

    if (fin == 999999999){
        cout << -1 << "\n";
    } else {
        cout << fin << "\n";
    }
    return 0;
}