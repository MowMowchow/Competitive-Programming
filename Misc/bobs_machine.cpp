#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
int N, M, R, s, e, v, j;
ll dp[1010];
vector<vector<ll>> jobs;


int bsearch(int x){
  int l = 0, r = jobs.size()-1, mid;
  while (l < r){
    mid = l+(r-l+1)/2;
    if (jobs[mid][1] == x){
      return mid;
    } else if (jobs[mid][1] < x){
      l = mid;
    } else {
      r = mid-1;
    }
  }
  return l;
}


int main(){
  cin >> N >> M >> R;
  for (int i = 0; i < M; i++){
    cin >> s >> e >> v;
    jobs.push_back({s, e+R, v});
  } jobs.push_back({0, 0, 0});

  sort(jobs.begin(), jobs.end(), [](const vector<ll> &a, const vector<ll> &b){return a[1] < b[1];});

  for (int i = 1; i < M+1; i++){
    j = bsearch(jobs[i][0]);
    dp[i] = max(jobs[i][2] + dp[j], dp[i-1]);
  }
  cout << dp[M] << "\n"; 
  return 0;
}