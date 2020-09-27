#include <bits/stdc++.h>
using namespace std;
long long N, temp;
bool primes[10000010], good;

void sieve(int n){
  for (int i = 2; i*i <= n; i++){
    if (primes[i]){
      for (int j = i*i; j <= n; j += i){
        primes[j] = false;
      }
    }
  }
}

int main(){
  memset(primes, true, sizeof(primes));
  sieve(10000010);

  cin >> N;

  for (int q = 0; q < N; q++){
    cin >> temp;
    if (temp > 1 && sqrt(temp)-floor(sqrt(temp)) == 0 && primes[(int)sqrt(temp)]){
      cout << "YES\n"; 
    } else {
      cout << "NO\n";
    }
  }

  return 0;
} 