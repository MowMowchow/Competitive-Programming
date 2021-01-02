#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, A[200010], temp = 1, finall = 0, l = 0, r = 0;

int main(){
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> A[i];
  }

  while (r < N){
    if (A[r] >= A[r+1]){
      finall = max(finall, r-l+1);
    } else {
      finall = max(finall, r-l+1);
      l = r+1; 
    }
    r++;
  }

  cout << finall << "\n";
  
  return 0;
}