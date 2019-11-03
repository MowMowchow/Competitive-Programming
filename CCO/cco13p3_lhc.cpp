#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

long long n, a, b, dists[400010], indegree[400010], backlength[400010], trunk, root[2] = {0, 0}, total[2] = {0, 0};  // root, length | length, occurrences
vector<int> adj[400010];


void dfs(int curr, int prev, int length){
    dists[curr] = length;

    if (length > root[1]){
        root[0] = curr;
        root[1] = length;
    }
    for (auto node : adj[curr]){
        if (prev != node){
            dfs(node, curr, length+1);
        }
    }
}

// case 1: explored branch length is equal to diameter
// case 2: new branch
// case 3: explored branch is same size as current
void dfs2(int curr, int prev){
    for (auto node : adj[curr]){
        if (prev != node){
            dfs2(node, curr);
            // have to -1 because length of current doesn't get updated yet
            if (backlength[curr] + backlength[node] == root[1]-1){
                total[0] = backlength[curr] + backlength[node]+1;
                total[1] += indegree[curr]*indegree[node];
            }
            // haha curr may not always be 0
            // erases the current length if it's shorter than the one recently explored
            if (backlength[curr] < backlength[node]+1){
                backlength[curr] = backlength[node]+1;
                indegree[curr] = indegree[node];
            }
            else if (backlength[curr] == backlength[node]+1){
                indegree[curr] += indegree[node];
            }


        }
    }
}


int main(){
    cin >> n;
    backlength[n] = 0; indegree[n] = 1;
    for (int i = 1; i < n; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        trunk = a;
        backlength[i] = 0;
        indegree[i] = 1;
    }

    // getting longest path from each node
    dfs(trunk, 0, 0);
    dfs(root[0], 0, 0);
    dfs2(root[0], 0);

    cout << total[0]+1 << " " << total[1] << "\n";
    return 0;
}