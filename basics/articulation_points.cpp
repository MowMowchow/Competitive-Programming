#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, M, a, b, parent[200000], low[200000], disc[200000], timee = 0;
bool vis[200000], ap[200000];
vector<int> adj[200000];


void dfs(int curr){
  vis[curr] = true;
  timee++;
  disc[curr] = timee;
  low[curr] = timee;
  int children = 0;
  for (auto node: adj[curr]){
    if (!vis[node]){
      children++;
      parent[node] = curr;
      dfs(node);
      low[curr] = min(low[curr], low[node]);
      if (parent[curr] == -1 && children > 1){
        ap[curr] = true;
      } if (parent[curr] != -1 && low[node] >= disc[curr]){
        ap[curr] = true;
      }
    }else if (parent[curr] != node){
      low[curr] = min(low[curr], disc[node]);
    }
  }
}


int main(){
  memset(vis, false, sizeof(vis));
  memset(ap, false, sizeof(ap));
  memset(parent, -1, sizeof(parent));
  memset(low, inf, sizeof(low));
  memset(disc, 0, sizeof(disc));

  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for (int i = 1; i <= N; i++){
    if (!vis[i]){
      dfs(i);
    }
  }

  for (int i = 1; i <= N; i++){
    cout << ap[i] << " ";
  } cout << "\n";

  return 0;
}