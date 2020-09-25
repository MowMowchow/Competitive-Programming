#include <bits/stdc++.h>
using namespace std;
int N, y, x, A, G;
string out;

int main(){
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> x >> y;
    if ((A+x)-G <= 500){
      A += x;
      out += "A";
    } else {
      G += y;
      out += "G";
    }
  }
  if (abs(A-G) > 500){
    cout << -1 << "\n";
  } else {
    cout << out << "\n";
  }
  return 0;
}