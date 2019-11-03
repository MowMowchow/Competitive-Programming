#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;

int n, t, x, y, w, total, dists1[200002], dists2[200002], finalroot = 0, root[2] = {0, 0}; // root[0] = root, root[1] = weight
vector<vector<int> > adj[200002];


void dfs(int curr, int prev, int weight){
    dists1[curr] = weight;
    if (root[1] < weight){
        root[0] = curr;
        root[1] = weight;
    }
    for (auto node : adj[curr]){
        if (prev != node[0]){
            dfs(node[0], curr, weight+node[1]);
        }
    }
}


int main() {
    cin.sync_with_stdio (0);
    cin.tie (0);

    cin >> n >> t;
    for (int i = 0; i < n-1; i++){
        cin >> x >> y >> w;
        adj[x].push_back({y, w});
        adj[y].push_back({x, w});
        total += w*2;
    }

    dfs(1, 0, 0);
    dfs(root[0], 0, 0);

    for (int i = 1; i < n+1; i++){
        dists2[i] = dists1[i];
        if (dists1[i] > dists1[finalroot]){
            finalroot = i;
        }
    }

    dfs(finalroot, 0, 0);

    for (int i = 1; i < n+1; i++){
        if (adj[i].size() == t){
            cout << i << " " << (total-max(dists1[i], dists2[i])) << "\n";
        }
    }
    return 0;
}