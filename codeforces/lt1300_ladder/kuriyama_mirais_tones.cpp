#include <bits/stdc++.h>
using namespace std;
long long N, M, L, R, T, arr[100010], psau[100010], psav[100010];


int main(){
  memset(arr, 0, sizeof(arr));
  memset(psau, 0, sizeof(psau));
  memset(psav, 0, sizeof(psav));

  cin >> N;
  
  for (int i = 0; i < N; i++){
    cin >> arr[i];
    psau[i+1] = psau[i] + arr[i];
    psav[i+1] = arr[i];
  }

  sort(psav, psav+N+1);

  for (int i = 0; i < N; i++) {
    psav[i+1] += psav[i];
  }

  cin >> M;

  for (int q = 0; q < M; q++){
    cin >> T >> L >> R;
    if (T == 1){
      cout << psau[R]-psau[L-1] << "\n";
    } else {
      cout << psav[R]-psav[L-1] << "\n";
    }
  }


  return 0;
}