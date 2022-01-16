#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

int N, M, a, b, ans = 0, rates[110], weights[2010], ctg[2010];
bool garage[110];
queue<int> q;


bool process(int car, bool enter){
  if (enter){
    for (int i = 0; i < N; i++){
      if (!garage[i]) {
        garage[i] = true;
        ctg[car] = i;
        ans += rates[i]*weights[car];
        return true;
      }
    }
  } else {garage[ctg[car]] = false;}
  return false;
}


int main(){
  memset(garage, false, sizeof(garage));
  cin >> N >> M;
  for (int i = 0; i < N; i++) cin >> rates[i];
  for (int i = 1; i <= M; i++) cin >> weights[i];

  for (int qq = 0; qq < 2*M; qq++) {
    cin >> a;
    if (a > 0) {
      if (!process(abs(a), 1)) {
        q.push(abs(a));
      }
    } else { // exit
        process(abs(a), 0);
        if (!q.empty()){
          process(abs(q.front()), 1);
          q.pop();
        }
    }
  }

  cout << ans << "\n";
  return 0;
}