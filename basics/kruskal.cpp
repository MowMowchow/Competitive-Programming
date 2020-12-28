#include <bits/stdc++.h>
using namespace std;
int N, M, a, b, c, x, y, w, subsets[200000][2];
vector<vector<int>> edges;


int find(int node){
  if (node != subsets[node][0]){
    subsets[node][0] = find(subsets[node][0]);
  }
  return subsets[node][0];
}


void unionn(int u, int v){
  if (subsets[u][1] > subsets[v][1]){
    subsets[v][0] = subsets[u][0];
  } else if (subsets[u][1] < subsets[v][1]){
    subsets[u][0] = subsets[v][0];
  } else {
    subsets[v][0] = subsets[u][0];
    subsets[u][1]++;
  }
}


int kruskal(){
  c = 0;
  int mst_weight = 0;

  for (auto edge: edges){
    a = edge[0]; b = edge[1]; w = edge[2];
    x = find(a), y = find(b);
    if (x != y){
      unionn(x, y);
      c++;
      mst_weight += w;
      if (c == N-1){
        break;
      }
    }

  }
  return mst_weight;
}


int main(){
  memset(subsets, 0, sizeof(subsets));
  cin >> N >> M;
  for (int i = 0; i < M; i++){
    cin >> a >> b >> c;
    subsets[a][0] = a;
    subsets[b][0] = b;
    edges.push_back({a, b, c});
  }

  sort(edges.begin(), edges.end(), [](const vector<int>&a, const vector<int>&b){return a[2] < b[2];});

  cout << kruskal() << "\n";

  return 0;
}