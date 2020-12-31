#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;


vector<int> kmp(string s, int n){
  vector<int> pi(n);
  int j;
  for (int i = 1; i < n; i++){
    j = pi[i-1];
    while (j > 0 && s[i] != s[j]){
      j = pi[j-1];
    }
    if (s[i] == s[j]){
      j++;
    }
    pi[i] = j;
  }
  return pi;
}


int kmp_search(string s, int n, string t, int m){
  vector<int> pi = kmp(s, n);
  s = "#"+s;
  int j = 0;
  for (int i = 0; i < m; i++){
    if (s[j+1] == t[i]){
      j++;
      if (j == n){
        return i-n+1;
      }
    } else {
      j = pi[j];
    }
  }
  return -1;
}


vector<int> kmp_oop(string s, int n){
  vector<int> pi = kmp(s, n);
  vector<int> ans(n+1);
  for (int i = 0; i < n; i++){
    ans[pi[i]]++;
  }
  for (int i = n-1; i > 0; i--){
    ans[pi[i-1]] += ans[i];
  } 
  for (int i = 0; i < n; i++){
    ans[i]++;
  }
  return ans;
}


int main(){
  cout << kmp_search("ababd", 5, "ababcabcabababd", 15) << "\n";
  return 0;
}