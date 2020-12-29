#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, M, a, b, timee = 0, disc[200000], low[200000];
bool vis[200000];
vector<int> adj[200000];


void dfs(int curr, int prev){
  vis[curr] = true;
  timee++;
  disc[curr] = timee;
  low[curr] = timee;

  for (auto node: adj[curr]){
    if (prev != node){
      if (vis[node]){
        low[curr] = min(low[curr], disc[node]);
      } else {
        dfs(node, curr);
        low[curr] = min(low[curr], low[node]);
        if (low[node] > disc[curr]){
          cout << curr << " - " << node << " is a bridge!\n";
        }
      }
    }
  }
}


int main(){
  memset(disc, 0, sizeof(disc));
  memset(low, inf, sizeof(low));
  memset(vis, false, sizeof(vis));
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for (int i = 1; i <= N; i++){
    if (!vis[i]){
      dfs(i, -1);
    }
  }

  return 0;
}