#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, T, M, q, totall = 0, players[300010];

int main(){
  memset(players, 0, sizeof(players));
  cin >> N >> T >> M;
  for (int i = 0; i < M; i++){
    cin >> q;
    if (players[q] != -1){
      players[q]++;
      if (players[q]+T-M > 0){
        players[q] = -1;
        totall++;
      }
    }
  }
  if (T-M > 0){
      cout << N << "\n";
  } else {
    cout << totall << "\n";
  }
  return 0;
}