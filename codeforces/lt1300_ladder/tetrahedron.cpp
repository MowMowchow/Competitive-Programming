#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll N, a = 0, b = 1, mod = 1000000007;

int main(){
  cin >> N;
  
  for (int i = 0; i < N; i++){
    int ta = (3*a)%mod;
    int tb = (2*a + b)%mod;
    a = tb % mod;
    b = ta % mod;
  }

  cout << b % mod;
  return 0;
}