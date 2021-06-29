#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
int N, L, S, a, b, s, curr = 0, total = 0;
vector<vector<int>> arr;


int main(){
  cin >> N >> L >> S;
  for (int i = 1; i <= N; i++){
    cin >> a >> b >> s;
    arr.push_back({a, s});  
    arr.push_back({b+1, -s});  
  }

  sort(arr.begin(), arr.end(), [](const std::vector<int>& a, const std::vector<int>& b) { return a[0] < b[0]; });

  for (int i = 0; i < arr.size(); i++){
    curr += arr[i][1];
    curr >= S ? total += arr[i+1][0]-arr[i][0]: 0;
  }

  cout << L-total << "\n";
  return 0;
}