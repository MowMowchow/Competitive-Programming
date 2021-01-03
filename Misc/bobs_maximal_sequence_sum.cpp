#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
long long N, arr[200010], total = 0;

int main(){
  memset(arr, 0, sizeof(arr));
  cin >> N;
  for (int i = 0; i < N-1; i++){
    cin >> arr[i];
  }
  total += arr[0] + arr[N-2];
  for (int i = 0; i < N-2; i++){
    total += min(arr[i], arr[i+1]);
  }
  cout << total << "\n";

  return 0;
}

