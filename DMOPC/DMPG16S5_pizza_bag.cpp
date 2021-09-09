#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

ll N, K, arr[200010], lmin[200010], ans, cs, j = 0;
map<ll, int> ck;

int main(){
  memset(arr, 0, sizeof(arr));

  cin >> N >> K;

  for (int i = 0; i < N; i++) cin >> arr[i];
  for (int i = 1; i <= K; i++) arr[(N-1)+i] = arr[i-1];
  for (int i = 1; i < N+K; i++) arr[i] += arr[i-1];

  j = 0;
  while (j < N+K){
    if (cs < K){
      cs++;
      ck[arr[j]]++;
      lmin[j] = ck.begin()->first;
      j++;
    } else {
      cs--;
      ck[arr[j-K]]--;
      if (!ck[arr[j-K]]) ck.erase(arr[j-K]);
    }
  }

  ans = arr[0];
  for (int i = 1; i < N+K; i++) ans = max(ans, arr[i]-lmin[i-1]);

  cout << ans << "\n";

  return 0;
}