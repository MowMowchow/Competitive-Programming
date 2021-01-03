#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
string s, alphabet = "abcdefghijklmnopqrstuvwyz";
int N, temp, finall = 0;
map<string, int> a, b;

int main(){
  cin >> N;
  cin >> s;

  for (auto letter: s){
    string let = to_string(letter);
    if (b.find(let) == b.end()){
      b[let] = 1; a[let] = 0;
    } else{
      b[let]++;
    }
  }

  for (auto letter: s){
    string let = to_string(letter);
    a[let]++; b[let]--;
    temp = 0;
    for (auto alph: alphabet){
      string alp = to_string(alph);
      if (a[alp] > 0 && b[alp] > 0){
        temp++;
      }
    }
    finall = max(finall, temp);
  }
  cout << finall << "\n";
  return 0;
}