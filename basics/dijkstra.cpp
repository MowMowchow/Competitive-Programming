#include <bits/stdc++.h>
using namespace std;
int N, M, a, b, c, dist[200000];
vector<vector<int>> adj[200000];
vector<int> curr;
const int inf = 0x3f3f3f3f;

struct Cmp {
    bool operator()(vector<int>&a, vector<int>&b){ return a[1] < b[1];}
};

void dijkstra(int start){
  priority_queue<vector<int>, vector<vector<int>>, Cmp> q;
  q.push({start, 0});
  dist[start] = 0;

  while(!q.empty()){
    curr = q.top(); q.pop();
    for (auto node: adj[curr[0]]){
      if (curr[1] + node[1] < dist[node[0]]){
        dist[node[0]] = curr[1] + node[1];
        q.push({node[0], dist[node[0]]});
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