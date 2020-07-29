#include <bits/stdc++.h>
using namespace std;
int n, x, y, vis[1100], final = 0;
vector<int> adj[1100];
map<int, bool> mapp;

void dfs(int curr, int length){
    if (!vis[curr]){
        vis[curr] = true;
        if (length >= 2) {
            if (mapp.find(curr) == mapp.end()){
                mapp[curr] = true;
            }
        }
        for (auto node: adj[curr]){
            dfs(node, length+1);
        }
    }
}


int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> x >> y;
        if (x != y){
            adj[x].push_back(y);}
    }

    for (int i = 1; i <= 1000; i++){
        memset (vis, false, sizeof(vis));
        dfs(i, 0);
    }

    for (auto item: mapp){
        final++;
    }

    cout << final << "\n";


    return 0;
}