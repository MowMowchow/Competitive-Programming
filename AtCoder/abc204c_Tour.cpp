#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

vector<int> adj[2010];
bool vis[2010];
int N, M, A, B, total = 0;


int dfs(int curr){
  if (!vis[curr]){
    vis[curr] = true; 

    int childCount = 1;
    for (auto node: adj[curr]){
      childCount += dfs(node);
    }
    return childCount;
  }
  return 0;
}


int main(){
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> A >> B;
    adj[A].push_back(B);
  }

  for (int i = 1; i <= N; i++){
    memset(vis, false, sizeof(vis));
    total += dfs(i);
  }

  cout << total << "\n";

  return 0;
}