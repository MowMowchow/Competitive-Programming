#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int n, m, x, y, w, dist[1002];
bool visited[1005] = {false};
vector<vector<int> > adj[1005];

void spfa(int a){
    queue<int> queue; queue.push(a);
    dist[a] = 0;

    while(!queue.empty()){
        int curr = queue.front(); queue.pop();
        visited[curr] = false;

        for (auto node : adj[curr]){
            if (dist[node[0]] > dist[curr] + node[1]){
                dist[node[0]] = dist[curr] + node[1];
                if (!visited[node[0]]){
                    visited[node[0]] = true;
                    queue.push(node[0]);
                }
            }
        }
    }
}


int main() {
    cin >> n >> m;
    fill(dist, dist+n+1, 9999999);
    for (int i = 0; i < m; i++){
        cin >> x >> y >> w;
         adj[x].push_back({y, w});
         adj[y].push_back({x, w});
    }

    spfa(1);

    for (int i = 1; i < n+1; i++){
        if (dist[i] != 9999999){
            cout << dist[i] << "\n";
        }
        else{
            cout << -1 << "\n";
        }
    }


    return 0;
}