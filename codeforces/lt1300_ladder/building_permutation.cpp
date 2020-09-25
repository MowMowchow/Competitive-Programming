#include <bits/stdc++.h>
using namespace std;
long long N, arr[300010], total = 0, prevlow = 0;

int main(){
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> arr[i];
  }

  sort(arr, arr+N);

  for (int i = 0; i < N; i++){
    if (arr[i] <= prevlow){
      prevlow++;
      total += prevlow-arr[i];
    } else {
      prevlow++;
      total += arr[i]-prevlow;
    }
  }

  cout << total << "\n";
  return 0;
}