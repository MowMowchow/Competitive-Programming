#include <bits/stdc++.h>
using namespace std;
string s;
int j = 0, i = 0, N, temp;
vector<int> lexarr;
vector<char> chararr;

int main(){
  cin >> s; N = s.length();

  while (i < N){
    temp = 0;
    for (int j = 0; j < N; j++){
      if (s[i] != s[i+j]){
        i = i+j-1;
        break;
      } else {
        temp++;
      }
    }
    lexarr.push_back(temp);
    i++;
  }

  return 0;
}