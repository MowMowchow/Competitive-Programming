#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
long long l, r, N, arr[300010], low, high, finall = inf;


int main(){
  memset(arr, 0, sizeof(arr));
  cin >> N;
  for (int i = 1; i <= N; i++){
    cin >> arr[i];
    arr[i] += arr[i-1];
  }
  l = 2; r = 2;
  while (l <= r){
    low = min(abs(arr[N]-arr[r]), min(abs(arr[r]-arr[l-1]), abs(arr[l-1]-arr[0])));
    high = max(abs(arr[N]-arr[r]), max(abs(arr[r]-arr[l-1]), abs(arr[l-1]-arr[0])));
    finall = min(finall, abs(high-low));
    if (abs(arr[r]-arr[l-1]) <= abs(arr[N]-arr[r])){ // moving r up
      r++;
      if (r == N){
        break;
      }
    }
    else {
      l++;
    } 
  }
  cout << finall << "\n";
  return 0;
}