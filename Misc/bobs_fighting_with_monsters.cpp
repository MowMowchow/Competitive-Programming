#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const long long ll_inf = LLONG_MAX;
long long N, K;

int main(){
  cin >> N >> K;
  if (N%K == 0){
    cout << 0 << "\n";
  } else {
    cout << min(N-K*(N/K), abs(N-K*((N/K)+1))) << "\n";
  }
  return 0;
}