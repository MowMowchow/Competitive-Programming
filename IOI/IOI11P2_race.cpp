#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;

int N, K, a, b, c, ans = 99999999;
vec2i adj[200010];
map<int, deque<int>> preDeq;
map<int, map<int, int>> preMap;
map<int, int> preHigh;

void up(int x, int length){
  cout << "inserting " << x << " with length " << length << "\n";
  // preDeq[x].push_back(length);
  preMap[x][length]++;
  cout << "preMap[" << x << "] = " << preHigh[x] << " updated to ";
  preHigh[x] = preMap[x].end()->first;
  cout << "preMap[" << x << "] = " << preHigh[x] << " preMap[" << x << "]: ";
  for (auto &p : preMap[x]){
    cout << p.first << " " << p.second << " | ";
  }
  cout << "\n";
}

void del(int x, int length){
  cout << "deleting " << x << " with length " << length << "\n";
  // preDeq[x].pop_back();
  preMap[x][length]--;
  if (!preMap[x][length]) preMap[x].erase(length);
  preHigh[x] = preMap[x].end()->first;
}


void dfs(int curr, int prev, int amt, int length){
  cout << "curr: " << curr << " | amt: " << amt << " | length: " << length << "\n";
  up(K-amt, length);
  if (preHigh[amt]) {
    cout << "it's working! | " << "length: " << length << " | preHigh[" << amt << "] = " << preHigh[amt] << "\n";
    ans = min(ans, length-preHigh[amt]);
  }
  for (auto node: adj[curr]){
    if (node[0] != prev){
      up(K-node[1], 1);
      dfs(node[0], curr, amt+node[1], length+1);
      del(K-node[1], 1);
    }
  }
  del(K-amt, length);
}


int main(){
  cin >> N >> K;
  for (int i = 1; i < N; i++){
    cin >> a >> b >> c;
    adj[a].push_back({b, c});
    adj[b].push_back({a, c});
  }

  dfs(0, -1, 0, 0);

  cout << ans << "\n";

  return 0;
}