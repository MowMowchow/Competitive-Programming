#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
const int capp = 3010;
int n, k, side;
long long triangle[capp][capp], bit[capp][capp], final;

void slowupdate(int i, int j, long long kk){ // why did i fucking try and make the triangle like the one in the input omf
    if (i > 0 && j > 0) {
        for (int ii = i; ii < capp; ii += (ii & -ii)) {
            for (int jj = j; jj < capp; jj += (jj & -jj)) {
                bit[ii][jj] = max(bit[ii][jj], kk);
            }
        }
    }
}

long long slowquery(int i, int j){ // change loop(s)
    long long total = 0;
    if (i > 0 && j > 0) {
        for (int ii = i; ii > 0; ii -= (ii & -ii)) {
            for (int jj = j; jj > 0; jj -= (jj & -jj)) {
                total = max(bit[ii][jj], total);
            }
        }
    }
    return total;
}

void printtri() {
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0) {
                cout << j << " ";
            }
            if (j == 0) {
                cout << i << " ";
            }
            if (i != 0) {
                cout << triangle[i][j] << " ";
            }
        }
        cout << "\n";
    }
}

int main(){
    cin >> n >> k;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            cin >> triangle[i][n-j+1];
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j <= i; j++){
            slowupdate(n-i+j, n-j, triangle[n-i+j][n-j]);
        }
        for (int j = 0; j <= i-k+1; j++){
            final += slowquery(n-(i-k+1)+j, n-j);
        }
    }
    cout << final;
}