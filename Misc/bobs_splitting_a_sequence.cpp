#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int l, r, N, arr[300010], s1, s2, s3;

// Nlogn
// fix middle block and use that to binary search
//  condition is to minimize abs(leftsum-rightsum)
int main(){
  cin >> N >> arr[0];
  for (int i = 1; i < N; i++){
    cin >> arr[i];
    arr[i] += arr[i-1];
  }

  
  return 0;
}