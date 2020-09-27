#include <bits/stdc++.h>
using namespace std;
long long N, arr[100010], arr2[100010], dp[100010], maxin = 0;

int main(){
  memset(dp, 0, sizeof(dp));
  memset(arr2, 0, sizeof(arr2));

  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> arr[i];
    arr2[arr[i]]++;
    maxin = max(maxin, arr[i]);
  }

  dp[1] = arr2[1];

  for (int i = 2; i <= maxin; i++){
    dp[i] = max((dp[i-2]+arr2[i]*i), dp[i-1]);
  }

  cout << dp[maxin] << "\n";
  return 0;
}