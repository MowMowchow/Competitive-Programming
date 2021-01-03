#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, h, M, q, arr[1000010];

int main(){
  memset(arr, 0, sizeof(arr));
  cin >> N >> M;
  for (int i = 0; i < N; i++){
    cin >> h;
    arr[h]++;
  }
  for (int i = 1000001; i > -1; i--){
    arr[i] += arr[i+1];
  }
  for (int i = 0; i < M; i++){
    cin >> q;
    cout << arr[q] << "\n";
  }
  return 0;
}