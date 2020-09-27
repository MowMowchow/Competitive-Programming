#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll N, Q, x, y, arr[200010], dif[200010], total = 0;

int main(){
  cin >> N >> Q;

  for (int i = 0; i< N; i++){
    cin >> arr[i];
  }

  for (int i = 0; i < Q; i++){
    cin >> x >> y;
    dif[x]++; dif[y+1]--;
  }

  for (int i = 1; i <= N; i++){
    dif[i] += dif[i-1];
  }

  sort(arr, arr+N);
  sort(dif, dif+N+1);

  for (int i = N; i > 0; i--){
    total += arr[i-1]*dif[i];
  }
  cout << total << "\n";
  return 0;
}