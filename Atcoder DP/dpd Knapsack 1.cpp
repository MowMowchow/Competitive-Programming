#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
long long dp[100010], n, w, ww, vv;

int main() {
    cin >> n >> w;
    for (int i = 1; i <= n; i++){
        cin >> ww >> vv;
        for (int j = w; j-ww >= 0; j--){
            dp[j] = max(dp[j], dp[j-ww] + vv);
        }
    }

    cout << dp[w];
    return 0;
}