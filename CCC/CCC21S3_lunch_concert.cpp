#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;
  
int N, p, w, d;
vec2ll ppl;


ll calc(ll c){
  ll total = 0, zero = 0;
  for (int i = 0; i < N; i++){
    total += max(zero, (abs(c-ppl[i][0])-ppl[i][2])*ppl[i][1]);
  }
  return total;
};


ll bsearch(){
  ll low = 0, high = 1000000000, mid, curr1, curr2, ans = LLONG_MAX;

  while (low < high){
    mid = low + (high-low)/2;
    curr1 = calc(mid);
    curr2 = calc(mid+1);

    ans = min(ans, min(curr1, curr2));
    if (curr1 < curr2){
      high = mid;
    } else{
      low = mid+1;
    }
  }
  return ans;
}


int main(){
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> p >> w >> d; // spot rate hearing
    ppl.push_back({p, w, d});
  }

  cout << bsearch() << "\n";

  return 0;
}