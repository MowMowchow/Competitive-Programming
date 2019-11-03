#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
int n, m, x, y, final = 0, dp[100005];
vector<int> adj[100005];

int dfs(int curr){
    if (dp[curr] != -1){
        return dp[curr];
    }
    else{
        dp[curr] = 0;
        for (auto &node: adj[curr]){
            dp[curr] = max(dp[curr], dfs(node)+1);
        }
    }
    return dp[curr];
}


int main() {
    memset(dp, -1, sizeof(dp));
    cin >> n >> m;
    for (int i = 0; i < m; i++){
        cin >> x >> y;
        adj[x].push_back(y);
    }

    for (int i = 1; i <= n; i++){
        final = max(final, dfs(i));
    }

    cout << final;

    return 0;
}