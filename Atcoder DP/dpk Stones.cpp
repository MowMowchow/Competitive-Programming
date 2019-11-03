#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
int n, k, moves[110], dp[100010], result;


int doo(int curr){
    if (curr < 0){
        return 0;
    }
    else if (dp[curr] != -1 || !dp[curr]){
        return dp[curr];
    }
    else{
        dp[curr] = 1;
        int temp = 0;
        for (int i = 0; i < n; i++){
            temp = !doo(curr-moves[i]);
            if (dp[curr] == 1 && temp == 1) {
                dp[curr] = 1;
            }
            else{
                dp[curr] = 0;
            }
        }
        return dp[curr];
    }
}


int main() {
    memset(dp, -1, sizeof(dp));
    cin >> n >> k;
    for (int i = 0; i < n; i++){
        cin >> moves[i];
    }

    result = doo(k);
    if (result == 1){
        cout << "Second\n";
    }
    else{
        cout << "First\n";
    }
    return 0;
}
