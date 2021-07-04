#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

int n, arr[110][110], dp[110][110], ans = 0;

int main(){
  cin >> n;
  for (int i = 0; i < n; i++){
    for (int j = 0; j <= i; j++){
      cin >> dp[i][j];
    }
  }

  for (int i = n-2; i > -1; i--){
    for (int j = i; j > -1; j--){
      dp[i][j] += max(dp[i+1][j+1], dp[i+1][j]);
    }
  }

  for (int i = 0; i < n; i++){
    ans = max(ans, dp[n-1][i]);
  }

  cout << dp[0][0] << "\n";
  return 0;
}