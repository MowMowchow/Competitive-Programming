#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
const int BIGGIE = 99999999;
using namespace std;

int s, n, e, x, y, w, u, curr, ouch, node, weight, sun, final = BIGGIE, dp[1610][3610];
vector<vector<int> > adj[1610];
vector<int> temp;

int main() {
    cin >> s >> n >> e;
    for (int i = 0; i < e; i++) {
        cin >> x >> y >> w >> u;

        adj[x].push_back({y, w, u});
        adj[y].push_back({x, w, u});
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < s+1; j++){
            if (i == 0){
                dp[i][j] = 0;
            }
            else{
            dp[i][j] = BIGGIE;
            }
        }
    }

    queue<vector<int> > queue;
    queue.push({0, 0});

    while(!queue.empty()){
        temp = queue.front(); queue.pop();
        curr = temp[0]; ouch = temp[1];

        if (curr == n-1){
            final = min(final, dp[curr][ouch]);
        }
        else if (!adj[curr].empty()) {
            for (auto temp1: adj[curr]) {
                node = temp1[0];
                weight = temp1[1];
                sun = temp1[2];

                if (((ouch + weight*sun) <= s) && (dp[node][ouch + weight*sun] > (dp[curr][ouch] + weight))) {
                    dp[node][ouch + weight*sun] = dp[curr][ouch] + weight;

                    if (final > dp[node][ouch + weight*sun]) {
                        vector<int> neww = {node, ouch + weight*sun};
                        queue.push(neww);
                    }
                }
            }
        }
    }

    if (final == BIGGIE){
        cout << -1 << "\n";
    }
    else {
        cout << final << "\n";
    }
    return 0;
}