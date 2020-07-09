#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int N, M, Q, blk[1010], wht[1010], visited[1010], dist[1010], a, b, c, curr, currb;
vector<vector<int>> adj[1010];
vector<int> temp;
queue<vector<int>> q;
string temps;

int main(){
    cin >> N >> M;
    memset(dist, 0x3f, sizeof(dist));
    memset(visited, false, sizeof(visited));

    for (int i = 0; i < M; i++){
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }

    temp = {1, 0, 0};
    q.push(temp);  // node, dist, brightness

    while (!q.empty()){
        temp = q.front(); q.pop();

        if (!visited[temp[0]]){
            visited[temp[0]] = true;
            dist[temp[0]] = temp[1];
            blk[temp[0]] = temp[2];
            wht[temp[0]] = temp[2];

            for (auto node: adj[temp[0]]){
                vector<int> temp2 = {node[0], temp[1]+1, temp[2]+node[1]};
                q.push(temp2);
            }

        } else if (visited[temp[0]] && temp[1] == dist[temp[0]]){
            blk[temp[0]] = min(blk[temp[0]], temp[2]);
            wht[temp[0]] = max(wht[temp[0]], temp[2]);
        }

    }

    cin >> Q;

    for (int i = 0; i < Q; i++){
        cin >> a >> temps;
        if (temps == "Black"){
            cout << dist[a] << " " << blk[a] << "\n";
        }else if (temps == "White"){
            cout << dist[a] << " " << wht[a] << "\n";
        }
    }


    return 0;
}