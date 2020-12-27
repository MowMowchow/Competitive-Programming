#include <bits/stdc++.h>
using namespace std;
int N, M, a, b, dist[200000];
vector<int> adj[200000];
bool visited[200000];


void bfs(int start){
  queue<vector<int>> q; q.push({start, 0});

  while (!q.empty()){
    vector<int> curr;
    curr = q.front(); q.pop();

    if (!visited[curr[0]]){
      visited[curr[0]] = true;
      dist[curr[0]] = curr[1];
      
      for (auto node: adj[curr[0]]){
        vector<int> temp = {node, curr[1]+1};
        q.push({temp});
      }
    } 
  }
}


int main(){
  memset(visited, false, sizeof(visited));
  memset(dist, 0, sizeof(dist));

  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  bfs(8);
  
  for (int i = 0; i <= N; i++){
    cout << dist[i] << " ";
  }

  return 0;
}