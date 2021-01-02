#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
int N, T, finall = 0, c, v;

int main(){
  cin >> N >> T;
  for (int i = 0; i < N; i++){
    cin >> c >> v;
    if (c < T){
      finall = max(finall, v);
    }
  }
  cout << finall << "\n";
  return 0;
}