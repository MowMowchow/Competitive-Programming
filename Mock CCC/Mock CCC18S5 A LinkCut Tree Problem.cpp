#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int n, m, q, a, b, c, qq, node, weight, subsets[1010][2]; // parent, rank
bool tempres = false, visited[1010];
vector<vector<int> > adj[1010];
vector<vector<int> > ogedges;

int find(int nodee){
    if (subsets[nodee][0] != nodee){
        return find(subsets[nodee][0]);
    }
    return subsets[nodee][0];
}

void unionn(int u, int v){
    if (subsets[u][1] > subsets[v][1]){
        subsets[v][0] = u;
    }
    else if (subsets[u][1] < subsets[v][1]){
        subsets[u][0] = v;
    }
    else{
        subsets[u][1]++;
        subsets[v][0] = u;
    }
}

void MST(){
    int u, v, w, x, y, counter = 0;
    vector<vector<int> > edges = ogedges;
    // initializing subsets (parent and rank)
    for (int i = 1; i <= n; i++){
        subsets[i][0] = i;
        subsets[i][1] = 0;
        adj[i].clear();
    }
    sort(edges.begin(), edges.end());

    for (int i = m-1; i >= 0; i--){
        vector<int> edge = edges[i];
        u = edge[1]; v = edge[2]; w = edge[0];
        x = find(u); y = find(v);

        if (x != y){
            counter++;
            unionn(x, y);
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        if (counter == n-1){
            return;
        }
    }
}

void update(int edgenum, int newweight){
    ogedges[edgenum-1][0] = newweight;
    MST();
}

bool bfs(int aa, int dest, int minw){ // just do bfs
    int curr;
    queue<int> queue; queue.push(aa);
    while (!queue.empty()){
        curr = queue.front(); queue.pop();
        visited[curr] = true;
        for (auto temp: adj[curr]){
            node = temp[0]; weight = temp[1];
            if (!visited[node] && weight >= minw){
                queue.push(node);
                if (node == dest){
                    return true;
                }
            }
        }
    }
    return false;
}


int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    cin >> n >> m;
    for (int i = 0; i < m; i++){
        cin >> a >> b >> c;
        ogedges.push_back({c, a, b, i+1});
    }

    MST();
    cin >> q;
    for (int i = 0; i < q; i++){
        cin >> qq;

        if (qq == 1){
            cin >> a >> b;
            update(a, b);
        }
        else if (qq == 2){
            cin >> a >> b >> c;
            memset(visited, false, sizeof(visited));
            tempres = bfs(a, b, c);
            if (tempres){
                cout << "1\n";
            }
            else{
                cout << "0\n";
            }
        }
    }
    return 0;
}