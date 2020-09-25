#include <bits/stdc++.h>
using namespace std;
int N, arr[110], final = 0, temp, psa[110];

int main(){
  memset(arr, 0, sizeof(arr));
  memset(psa, 0, sizeof(psa));

  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> arr[i];
    psa[i+1] += arr[i]+psa[i];
  }

  for (int i = 0; i < N; i++){
    if (arr[i] == 0){
      for (int j = i; j < N; j++){
        final = max(final, psa[i] + ((j-i+1)-(psa[j+1]-psa[i])) + (psa[N]-psa[j]));      
      }
    } else {
        for (int j = i+1; j < N; j++){
        final = max(final, psa[i] + ((j-i+1)-(psa[j+1]-psa[i])) + (psa[N]-psa[j]));      
      }
    }

  }
  cout << final << "\n";
  return 0;
}