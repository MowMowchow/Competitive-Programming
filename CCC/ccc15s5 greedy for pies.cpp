#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int N, M;
int ogpies[3005], insert[105];
int dp[3005][2][105][105];


int doo(int curr, int take, int l , int r){
    //cout << curr << "\n";
    int& temp = dp[curr][take][l][r];

    if (temp != -1){
        return temp;
    }
    if(curr == N+1) {
        if (l <= r) {
            if (take == 1) {
                temp = insert[r] + doo(curr, 0, l, r - 1);
                return temp;
            } else if (take == 0) {
                temp = doo(curr, 1, l + 1, r);
                return temp;
            }
        }
        else {
            temp = 0;
            return temp;

        }
    }
    else if(take == 1){
        temp = max(doo(curr, 0, l, r), ogpies[curr] + doo(curr+1, 0, l, r));
        if (l <= r){
            temp = max(temp, insert[r] + doo(curr, 0, l, r-1));
        }
    }
    else{
        temp = doo(curr+1, 1, l, r);
        if (l <= r){
            temp = max(temp, doo(curr, 1, l+1, r));
        }
    }
    return temp;
}


int main() {
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int i = 1; i <= N; i++){
        int t; cin >> t;
        ogpies[i] = t;
    }
    cin >> M;
    for (int i = 1; i <= M; i++){
        int t; cin >> t;
        insert[i] = t;
    }

    memset(dp, -1, sizeof dp);
    sort(insert+1, insert+1+M);

    cout << doo(1, 1, 1, M);
    return 0;
}