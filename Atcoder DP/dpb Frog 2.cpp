#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
int dp[100010], stones[100010], n, k;

int main() {
    //memset(dp, 9999, sizeof(dp));
    cin >> n >> k;
    for (int i = 1; i <= n; i++){
        cin >> stones[i];
        dp[i] = 999999999;
    }

    dp[1] = 0;
    for (int i = 1; i < n; i++){
        for (int j = 1; j <= k; j++){
            if (i+j <= n){
                dp[i+j] = min(dp[i+j], abs(stones[i]-stones[i+j])+dp[i]);
            }
        }
    }

    cout << dp[n];
    return 0;
}