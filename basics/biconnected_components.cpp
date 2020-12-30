#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, M, a, b, t = 0, low[200000], disc[200000];
bool vis[200000];
vector<int> adj[200000];
vector<vector<int>> s;
vector<vector<vector<int>>> components;


void dfs(int curr, int prev){
  vis[curr] = true;
  t++;
  disc[curr] = t;
  low[curr] = t;
  int children = 0;
  for (auto node: adj[curr]){
    if (prev != node){
      if (vis[node] && low[curr] > disc[node]){
        low[curr] = min(low[curr], disc[node]);
        s.push_back({curr, node});
      } else if (!vis[node]){
        s.push_back({curr, node});
        children++;
        dfs(node, curr);
        low[curr] = min(low[curr], low[node]);
        if (prev == -1 && children > 1){
          vector<vector<int>> temp;
          while (s.size() > 0){
            if (s.back() == vector<int>{curr, node}){
              temp.push_back(s.back()); s.pop_back();
              break;
            }
            temp.push_back(s.back()); s.pop_back();
          }
          components.push_back(temp);
        } else if (low[node] >= disc[curr]){
          vector<vector<int>> temp;
          while (s.size() > 0){
            if (s.back() == vector<int>{curr, node}){
              temp.push_back(s.back()); s.pop_back();
              break;
            }
            temp.push_back(s.back()); s.pop_back();
          }
          components.push_back(temp);
        }
      }
    }
  }
}


int main(){
  memset(low, inf, sizeof(low));
  memset(disc, 0, sizeof(disc));
  memset(vis, false, sizeof(vis));
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for (int i = 0; i < N; i++){
    if (!vis[i]){
      s.clear();
      dfs(i, -1);
    }
  }

  for (auto component: components){
    for (auto edge: component){
      for (auto node: edge){
        cout << node << " ";
      }cout << " | ";
    } cout << " \n";
  }

  return 0;
}