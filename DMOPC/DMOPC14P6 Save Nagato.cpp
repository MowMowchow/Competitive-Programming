#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;

int n, trunk, root[2] = {-1, 0}, dists1[500002], dists2[500002]; // root[0] = root, root[1] = length
vector<int> adj[500002];


void dfsdia(int curr, int prev, int length){
    dists1[curr] = length;
    if (length > root[1]){
        root[0] = curr;
        root[1] = length;
    }
    for (auto node: adj[curr]){
        if (node != prev){
            dfsdia(node, curr, length+1);
        }
    }
}


int main() {
    cin >> n;
    for (int i = 0; i < n-1; i++){
        int x, y; cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
        trunk = x;
    }

    // diameter of tree
    dfsdia(trunk, 0, 1);
    dfsdia(root[0], 0, 1);
    copy(begin(dists1), end(dists1), begin(dists2));
    dfsdia(root[0], 0, 1);

    for (int i = 1; i < n+1; i++){
        cout << max(dists1[i], dists2[i]) << "\n";
    }
    return 0;
}