#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
long long N, K, ans = 1;

int main(){
  cin >> K >> N;

  for (int i = 0; i < K; i++){
    ans *= N;
  }
  cout << ans << "\n";
  return 0;
}