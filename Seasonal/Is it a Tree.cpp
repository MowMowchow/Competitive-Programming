#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
const int BIGGIE = 964478;
using namespace std;
int adj[5][5], root, total = 0, nodecount = 0;
bool visited[5] = {false};


int dfs(int curr){
    total++;
    visited[curr] = true;
    for (int node = 1; node < 5; node++){
        if (adj[curr][node] == 1 && !visited[node]){
            dfs(node);
        }
    }
    return total;
}



int main() {
    for (int i = 1; i < 5; i++){
        for (int j = 1; j < 5; j++){
            cin >> adj[i][j];
            nodecount += adj[i][j];
            if (adj[i][j]){
                root = i;
            }
        }
    }
    dfs(root);
    if (nodecount == 6){
        if (total == 4) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }
    else {
        cout << "No\n";
    }
    return 0;
}