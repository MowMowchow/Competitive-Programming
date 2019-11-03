#include <iostream>
#include <algorithm>
using namespace std;
int dp[100005][3], n, items[100005][3];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> items[i][0] >> items[i][1] >> items[i][2];
    }
    for (int i = 1; i <= n; i++){
        for (int j = 0; j < 3; j++){
            for (int k = 0; k < 3; k++){
                if (j != k) {
                    dp[i][k] = max(dp[i][k], dp[i-1][j] + items[i-1][k]);
                    //dp[i+1][k] = max(dp[i+1][k], dp[i][j] + items[i][k]);
                }
            }
        }
    }
    cout << max(dp[n][0], max(dp[n][1], dp[n][2]));
    return 0;
}