#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

ll N, M, a, b, C, A, B, l, r;
vec2ll adj[100010];
vec1ll dist(100010);

bool dijkstra(int cap){
  priority_queue<vec1ll, vec2ll, greater<vec1ll>> pq;
  pq.push({0, A});
  fill(dist.begin(), dist.end(), LONG_LONG_MAX);
  dist[A] = 0;
  while (!pq.empty()){
    vec1ll curr = pq.top(); pq.pop();
    if (curr[1] == B) return curr[0] <= C ? true : false;
    if (curr[0] > dist[curr[1]]) continue;
    for (auto node: adj[curr[1]]){
      if (curr[0]+node[1] < dist[node[0]] && node[2] <= cap)
      dist[node[0]] = curr[0]+node[1];
      pq.push({dist[node[0]], node[0]});
    }
  }
  return dist[B] <= C ? true : false;
}

int bs(){
  int l = 1, r = M, ans = -1;

  while (l <= r){
    int mid = l+(r-l+1)/2;
    if (dijkstra(mid)){
      ans = mid;
      r = mid-1;
    } else l = mid + 1;
  }
  return ans;
}


int main(){
  cin >> N >> M;
  for (int i = 1 ; i <= M; i++)  {
    cin >> a >> b >> C;
    adj[a].push_back({b, C, i});
    adj[b].push_back({a, C, i});
  }
  cin >> A >> B >> C;

  cout << bs() << "\n";
  return 0;
}