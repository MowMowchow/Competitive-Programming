#include <bits/stdc++.h>
using namespace std;
string s, out = "";
int N, NN;
bool skip;

int main(){
  cin >> s; N = s.length();

  for (int i = 0; i < N; i++){
    NN = out.length();
    skip = false;
    if (NN > 1){
      if (out[NN-2] == out[NN-1] && out[NN-1] == s[i]) skip = true;
    } if (NN > 2){
      if (out[NN-3] == out[NN-2] && out[NN-1] == s[i]) skip = true;
    }
    if (!skip) out += s[i];
  }

  cout << out << "\n";
  return 0;
}