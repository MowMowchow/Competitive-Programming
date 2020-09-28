#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll N, K, D, dp[110][2], mod = 1000000007;

int main(){
  cin >> N >> K >> D;

  dp[0][0] = 1; dp[0][1] = 0;

  for (ll i = 1; i <= N; i++){
    for (ll j = 1; j <= min(K, i); j++){
      if (j < D){
        dp[i][0] += dp[i-j][0];
        dp[i][1] += dp[i-j][1];
      } else {
        dp[i][1] += dp[i-j][0] + dp[i-j][1];
      } 
      dp[i][0] %= mod;    
      dp[i][1] %= mod;    
    }
  }

  cout << dp[N][1] << "\n";
  return 0;
}