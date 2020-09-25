#include <bits/stdc++.h>
using namespace std;
int N, M, suffix[100010], arr[100010], temp;
map<int, bool> nums;

int main(){
  memset(suffix, 0, sizeof(suffix));
  cin >> N >> M;

  for (int i = 0; i < N; i++){
    cin >> arr[i];
    
  }

  for (int i = N-1; i > -1; i--){
    if (nums.find(arr[i]) == nums.end()){
      nums[arr[i]] = true;
      suffix[i]+= suffix[i+1]+1;
    } else {
      suffix[i] = suffix[i+1];
    }
  }

  for (int i = 0; i < M; i++){
    cin >> temp;
    cout << suffix[temp-1] << "\n";
  } cout << "\n";

  return 0;
}
