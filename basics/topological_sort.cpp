#include <bits/stdc++.h>
using namespace std;
int N, M, a, b;
bool visited[200000];
vector<int> adj[200000];
vector<int> stackk;


void dfs(int curr){
  visited[curr] = true;

  for (auto node: adj[curr]){
    if (!visited[node]){
      dfs(node);
    }
  }
  stackk.push_back(curr);
}


int main(){
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b;
    adj[a].push_back(b);
  }


  for (int i = 0; i < N; i++){
    if (!visited[i]){
      dfs(i);
    }
  }

  for (int i = N-1; i >= 0; i--){
    cout << stackk[i] << " ";
  }cout << "\n";
  
  return 0;
}   