#include <bits/stdc++.h>
using namespace std;

int R, C, arr[510][510], temp, final = 9999999, q;
bool prime[1000010];
vector<int> primes;


void sieve(int n) {
  prime[0] = false; prime[1] = false;
  for (int i = 2; i <= sqrt(n); i++){
    if (prime[i]){
      for (int j = i*2; j <= n; j += i){
        prime[j] = false;
      }
    }
  }
  for (int i = 2; i <= 1000000; i++){
    if (prime[i]){
      primes.push_back(i);
    }
  }
}


int binup(int x){
  int low = 0; int high = primes.size()-1;

  while (low < high){
    int mid = low + ((high-low)/2);

    if (primes[mid] < x) {
      low = mid+1;
    } else {
      high = mid;
    }
  }
  return low;
}


int main(){
  memset(prime, true, sizeof(prime));
  sieve(1000000);

  cin >> R >> C;

  for (int i = 0; i < R; i++){
    for (int j = 0; j < C; j++){
      cin >> arr[i][j];
    }
  }

  // calc for rows -> horizontal
  for (int i = 0; i < R; i++){
    temp = 0;
    for (int j = 0; j < C; j++){
     q = arr[i][j];
      if (!prime[q]){
        if (q < 2){
          temp += 2-q;
        } else {
          temp += primes[binup(q)]-q;
        }     
      }
    }
    final = min(final, temp);
  }

  // calc for cols -> vertical
  for (int i = 0; i < C; i++){
    temp = 0;
    for (int j = 0; j < R; j++){
      q = arr[j][i];
      if (!prime[q]){
        if (q < 2){
          temp += 2-q;
        } else {
          temp += primes[binup(q)]-q;
        }     
      }
    }
    final = min(final, temp);
  }

  cout << final << "\n";
  return 0;
}