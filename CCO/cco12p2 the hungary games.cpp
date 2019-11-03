#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
const int BIGGIE = 96469478;
using namespace std;

int n, m , x, y, w, curr, nextt, weight, final[2] = {BIGGIE, BIGGIE}, dists1[20010], dists2[20010];
vector<vector<int> > foradj[20010];
vector<vector<int> > revadj[20010];
vector<vector<int> > edges;


void spfa1(int a){
    bool visited[20010] = {false};
    queue<int> queue; queue.push(a);
    dists1[a] = 0;

    while (!queue.empty()){
        curr = queue.front(); queue.pop();
        visited[curr] = false;

        for (auto node: foradj[curr]){
            nextt = node[0]; weight = node[1];
            if (dists1[nextt] > dists1[curr] + weight){
               dists1[nextt] = dists1[curr] + weight;
               if (!visited[nextt]){
                   visited[nextt] = true;
                   queue.push(nextt);
               }
            }
        }
    }
}

void spfa2(int a){
    bool visited[20010] = {false};
    queue<int> queue; queue.push(a);
    dists2[a] = 0;

    while (!queue.empty()){
        curr = queue.front(); queue.pop();
        visited[curr] = false;

        for (auto node: revadj[curr]){
            nextt = node[0]; weight = node[1];
            if (dists2[nextt] > dists2[curr] + weight){
               dists2[nextt] = dists2[curr] + weight;
               if (!visited[nextt]){
                   visited[nextt] = true;
                   queue.push(nextt);
               }
            }
        }
    }
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> w;
        foradj[x].push_back({y, w});
        revadj[y].push_back({x, w});
        edges.push_back({x, y, w});
    }
    for (int i = 0; i <= n; i++){
        dists1[i] = BIGGIE; dists2[i] = BIGGIE;
    }

    spfa1(1);
    spfa2(n);


    for (auto edge: edges){
        x = edge[0]; y = edge[1]; weight = edge[2];
        if (dists1[x] != BIGGIE && dists2[y] != BIGGIE){
            curr = dists1[x] + weight + dists2[y];
            if (curr < final[0]){
                final[1] = final[0];
                final[0] = curr;
            }
            else if(curr > final[0] && curr < final[1]){
                final[1] = curr;
            }
        }
    }
    if (final[1] != BIGGIE){
        cout << final[1] << "\n";
    }
    else{
        cout << -1 << "\n";
    }

    return 0;
}