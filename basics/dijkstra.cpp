#include <bits/stdc++.h>
using namespace std;
int N, M, a, b, c, curr, dist[200000];
vector<vector<int>> adj[200000];
const int inf = 0x3f3f3f3f;


void dijkstra(int start){
  priority_queue<int> q; q.push(start);
  dist[start] = 0;

  while(!q.empty()){
    curr = q.top(); q.pop();
    for (auto node: adj[curr]){
      if (dist[curr] + node[1] < dist[node[0]]){
        dist[node[0]] = dist[curr] + node[1];
        q.push(node[0]);
      }
    }
  }
}


int main(){
  memset(dist, inf, sizeof(dist));
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b >> c;
    adj[a].push_back({b, c});
    adj[b].push_back({a, c});
  }
  
  dijkstra(1);

  for (int i = 0; i <= N; i++){
    cout << dist[i] << " ";
  } cout << "\n";

  return 0;
}