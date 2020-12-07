#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll M, A, C, X, N, G, cycle = 1, base;

map<int, bool> vis;


int main(){
  cin >> M >> A >> C >> X >> N >> G;
  base = X;

  for (int i = 0; i < N; i++){  
    X = ((A*X) + C) % M;  
    if (vis.find(X) == vis.end()){
      vis[X] = true;
      cycle++;
    } else if (vis[X]) {
      // cout << "CYCLE\n";
      break;
    }
  }

  N %= cycle;
  X = base;

  for (int i = 0; i < N; i++){
    X = ((A*X) + C) % M;
  }

  cout << X % G << "\n";

  return 0;
}