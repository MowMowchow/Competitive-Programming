#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, M, a, b, timee = 0, low[200000], disc[200000];
bool vis[200000], instack[200000];
vector<int> adj[200000], stackk;
vector<vector<int>> total_scc;


void tarjan(int curr, int prev){
  stackk.push_back(curr);
  instack[curr] = vis[curr] = true;
  disc[curr] = low[curr] = timee++;
  for (auto node: adj[curr]){
    if (!vis[node]){
      tarjan(node, curr);
    } if (instack[node]){
      low[curr] = min(low[curr], low[node]);
    }
  }
  if (disc[curr] == low[curr]){
    vector<int> temp;
    while (stackk.size() > 0){
      instack[stackk.back()] = false;
      low[stackk.back()] = disc[curr];
      if (stackk.back() == curr){
        temp.push_back(stackk.back()); stackk.pop_back();
        break;
      }
      temp.push_back(stackk.back()); stackk.pop_back();
    }
    total_scc.push_back(temp);
  }
}


int main(){
  memset(low, inf, sizeof(low));
  memset(disc, 0, sizeof(disc));
  memset(vis, false, sizeof(vis));
  memset(instack, false, sizeof(instack));
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
  }

  for (int i = 1; i <= N; i++){
    if (!vis[i]){
      tarjan(i, -1);
      stackk.clear();
    }
  }

  for (auto scc: total_scc){
    for (auto node: scc){
      cout << node << " ";
    } cout << "\n";
  }
  return 0;
}
