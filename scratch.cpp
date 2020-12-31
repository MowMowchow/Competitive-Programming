#include <bits/stdc++.h>
using namespace std;

vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i-1];
        while (j > 0 && s[i] != s[j])
            j = pi[j-1];
        if (s[i] == s[j])
            j++;
        // cout << "at i: " << i << " | j: " << j << " | pi[i-1]: " << pi[i-1] << " | pi[i]: " << pi[i] << "\n";
        pi[i] = j;
    }
    return pi;
}

int main(){
  string s = "aabaaab";
  int n = s.length();
  vector<int> pi;
  pi = prefix_function(s);
  for (auto let: pi){
    cout << let << " ";
  } cout << "\n";

  vector<int> ans(n + 1);
  for (int i = 0; i < n; i++)
      ans[pi[i]]++;

  for (auto ind: ans){
    cout << ind << " ";
  } cout << "\n";

  for (int i = n-1; i > 0; i--)
      ans[pi[i-1]] += ans[i];

  for (auto ind: ans){
  cout << ind << " ";
  } cout << "\n";

  for (int i = 0; i <= n; i++)
      ans[i]++;
  
  for (auto ind: ans){
    cout << ind << " ";
  } cout << "\n";
  
  return 0;
}