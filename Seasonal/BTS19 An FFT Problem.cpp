#include <iostream>
#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll n, a, dp[2010][2010], arr[2010], mod = 998244353;


int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a;
        arr[i] = a;
    }

    for (int i = 0; i <= n; i++){
        dp[0][i] = 1;
    }
    for (int i = 1; i <= n; i++){
        dp[i][i] = 1;
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            dp[i][i] = (mod + (dp[i][i] * arr[j])%mod)%mod;
        }
        for (int j = i+1; j <= n; j++){
            dp[i][j] = ((dp[i][j-1] + dp[i-1][j-1]*arr[j])%mod + mod)%mod;
        }
    }

    for (int i = 1; i <=n; i++){
        cout << dp[i][n]%mod << " ";
    }
    return 0;
}