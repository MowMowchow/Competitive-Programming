#include <bits/stdc++.h>

using namespace std;

const int MAX = 100001;
int n, w;
long long dp[MAX];

int main(){
    cin >> n >> w;
    memset(dp, 0x3f, sizeof(dp));
    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        int x, y; cin >> x >> y;
        for(int j = MAX - 1; j >= y; j--){
            dp[j] = min(dp[j], dp[j - y] + x);
        }
    }

    int best = -1;
    for (int i = 0; i < MAX; i++){
        if(dp[i] <= w){
            best = i;
        }
    }

    cout << best;
    return 0;
}