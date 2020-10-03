#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int N, A, B, maxval = 0;
vector<vector<int>> arr;

int main(){
  
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> A >> B;
    arr.push_back({A, B});
  }

  sort(arr.begin(), arr.end());

  maxval = min(arr[0][0], arr[0][1]);

  for (int i = 1; i < N; i++){
    if (maxval <= arr[i][1]){
      maxval = arr[i][1];
    } else {
      maxval = arr[i][0];
    }
  }
  cout << maxval << "\n";
  return 0;
}