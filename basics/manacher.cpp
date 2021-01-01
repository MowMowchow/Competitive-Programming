#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
string s;
vector<int> ans;


vector<int> manacher(string s){
  int n = s.size();
  vector<int> d1(n+1);
  vector<int> d2(n+1);
  vector<int> temp(n+1);
  for (int i = 0, l = 0, r = -1, k; i < n; i++){
    k = (i > r ? 1: min(d1[l+r-i], r-i+1));
    while(0 <= i-k && i+k < n && s[i-k] == s[i+k]){
      k++;
    }
    d1[i] = k--;
    if (i+k > r){
      l = i-k;
      r = i+k;
    }
  }
  for (int i = 0, l = 0, r = -1, k; i < n; i++){
    k = (i > r ? 0: min(d2[l+r-i+1], r-i+1));
    while(0 <= i-k-1 && i+k < n && s[i-k-1] == s[i+k]){
      k++;
    }
    d2[i] = k--;
    if (i+k > r){
      l = i-k-1;
      r = i+k;
    }
  }
  for (int i = 0; i < n; i++){
    temp[i] = max((d1[i]*2)-1, d2[i]*2);
  }
  return temp;
}


int main(){
  cin >> s;
  
  ans = manacher(s);

  for (auto ind: ans){
    cout << ind << " ";
  } cout << "\n";

  return 0;
}