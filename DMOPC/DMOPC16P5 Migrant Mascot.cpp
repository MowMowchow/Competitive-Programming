#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

const int BIGNUM = 0x3f3f3f3f;
int n, m;
vector<vector<int> > edges;
int ogsubsets[200005][2];  // parent, rank
int answers[200005];
vector<vector<int> > mst;
vector<vector<int> > adj[200005];


int find(int node){
    if (ogsubsets[node][0] != node){
        ogsubsets[node][0] = find(ogsubsets[node][0]);
    }
    return ogsubsets[node][0];
}

void unionn(int u, int v){
    if (ogsubsets[u][1] > ogsubsets[v][1]){
        ogsubsets[v][0] = ogsubsets[u][0];
    }
    else if (ogsubsets[u][1] < ogsubsets[v][1]){
        ogsubsets[u][0] = ogsubsets[v][0];
    }
    else{
        ogsubsets[u][1] += 1;
        ogsubsets[v][0] = ogsubsets[u][0];
    }
}

void kruskal(){
    for (int i = 0; i < m; i++){
        int u, v, w, x, y;
        w = edges[i][0]; u = edges[i][1]; v = edges[i][2];
        x = find(u); y = find(v);
        if (x != y){
            unionn(x, y);
            vector<int> temp; temp.push_back(u); temp.push_back(v); temp.push_back(w);
            mst.push_back(temp);
            if (i == n-1){
                break;
            }
        }
    }
}

void dfs(int curr, int weight, int prev){
    answers[curr] = weight;
    for (auto node: adj[curr]){
        if (node[0] != prev){
            dfs(node[0], min(weight, node[1]), curr);
        }
    }
}

int main() {
    fill_n(answers, 200005, BIGNUM);
    cin >> n >> m;

    //setting up the graph
    for (int i = 0; i < m; i++){
        int x, y, w; cin >> x >> y >> w;
        vector<int> temp;
        temp.push_back(w); temp.push_back(x); temp.push_back(y);
        edges.push_back(temp);
    }
    sort(edges.begin(), edges.end());
    reverse(edges.begin(), edges.end());
    //prepping the disjoint sets
    for (int i = 0; i < 200005; i++){
        ogsubsets[i][0] = i; ogsubsets[i][1] = 0;
    }
    kruskal();

    //adj list to traverse with dfs
    for (auto edge: mst){
        int x, y, w; x = edge[0]; y = edge[1]; w = edge[2];
        vector<int> temp1; temp1.push_back(y); temp1.push_back(w);
        adj[x].push_back(temp1);
        vector<int> temp2; temp2.push_back(x); temp2.push_back(w);
        adj[y].push_back(temp2);
    }

    dfs(1, BIGNUM, 0);

    for (int i = 1; i < n+1; i++){
        if (answers[i] == BIGNUM){
            cout << 0 << "\n";
        }
        else{
            cout << answers[i] << "\n";
        }
    }
    return 0;
}