#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
const int BIGGIE = 964478;
using namespace std;
int n, m, a, b, w, dist1[5010], dist2[5010], curr, node, weight, kur1, kur2;
vector<vector<int> > adj[5010];


void spfa(){
    //bool visited[5010] = {false};
    queue<int> queue; queue.push(1);
    dist1[1] = 0;
    while (!queue.empty()){
        curr = queue.front(); queue.pop();
        //visited[curr] = false;

        for (auto temp: adj[curr]){
            node = temp[0]; weight = temp[1];
            kur1 = dist1[curr] + weight; kur2 = dist2[curr] + weight;

            if (kur1 < dist1[node]){
                dist2[node] = dist1[node];
                dist1[node] = kur1;
                //visited[node] = true;
                queue.push(node);
            }
            else if (dist1[node] != kur1 && kur1 < dist2[node]){
                dist2[node] = kur1;
                //visited[node] = true;
                queue.push(node);
            }
            else if (dist1[node] != kur2 && kur2 < dist2[node]){
                dist2[node] = kur2;
                //visited[node] = true;
                queue.push(node);
            }
        }
    }
}



int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++){
        cin >> a >> b >> w;
        adj[a].push_back({b, w});
        adj[b].push_back({a, w});
    }
    for (int i = 0; i <= n; i++){
        dist1[i] = BIGGIE; dist2[i] = BIGGIE;
    }

    spfa();

    if (dist2[n] == BIGGIE){
        cout << "-1\n";
    }
    else{
        cout << dist2[n] << "\n";
    }
    return 0;
}