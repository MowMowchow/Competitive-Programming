#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
// find min radius for each tree
// sort radii
// add first two +L, vs 2nd and 3rd + 2L
vector<vector<int> > adj[100010];
vector<int> radii;
bool visited[100010];
int bigdiam = 0, paths[100010], dists[100010];


void dfs(int curr, int prev, int length, int &root, int &dia){
    visited[curr] = true;
    paths[curr] = prev;
    if (length > dia){
        root = curr;
        dia = length;
    }
    for (auto temp: adj[curr]){
        int node = temp[0], weight = temp[1];
        if (node != prev){
            dists[node] = weight;
            dfs(node, curr, length+weight, root, dia);
        }
    }
}



int travelTime(int N, int M, int L, int A[], int B[], int T[]){
    for (int i = 0; i < M; i++){
        adj[A[i]].push_back({B[i], T[i]});
        adj[B[i]].push_back({A[i], T[i]});
    }
    memset(visited, false, sizeof(visited));
    memset(paths, -1, sizeof(paths));

    for (int i = 0; i < N; i++){
        if (paths[i] == -1){
            int rootnode = i, rootdia = 0;
            dfs(i, i, 0, rootnode, rootdia);
            rootdia = 0;
            dfs(rootnode, rootnode, 0, rootnode, rootdia);
            bigdiam = max(bigdiam, rootdia);
            int currradius = rootdia, currtotal = 0;

            for (int j = rootnode; j != paths[j]; j = paths[j]){
                currradius = min(currradius, max(currtotal, rootdia-currtotal));
                currtotal += dists[j];
            }
            radii.push_back(currradius);
        }
    }
    sort(radii.rbegin(), radii.rend());
    
    if (1 < radii.size()){
        bigdiam = max(bigdiam, radii[0]+radii[1]+L);
    }
    if (2 < radii.size()){
        bigdiam = max(bigdiam, radii[1]+radii[2]+(2*L));
    }
    return bigdiam;
    //cout << bigdiam;
}