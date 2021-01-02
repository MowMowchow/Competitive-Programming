#include <bits/stdc++.h>
using namespace std;



int main(){
  string s = "#a#b#a#a#b#c#";
  int n = s.size();
  vector<int> d1(n);
  int k;
  for (int i = 0; i < n; i++){
    cout << i << " ";
  } cout << "\n";
  for (auto let: s){
    cout << let << " ";
  }cout << "\n";
  for (int i = 0, l = 0, r = -1; i < n; i++) {
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    cout << "at i: " << i << " | l: " << l << " | r: " << r << " \n";
    if (i > r){
      k = 1;
    } else {
      if (d1[l+r-i] > r-i+1){
        k = r-i+1;
        cout << "d1[l+r-i] = " << d1[l+r-i] << " > " << " r-i+1 = " <<  r-i+1 << "\n";
      } else if (d1[l+r-1] < r-i+1){
        k = d1[l+r-1];
        cout << "d1[l+r-i] = " << d1[l+r-i] << " < " << " r-i+1 = " <<  r-i+1 << "\n";
      } else {
        k = d1[l+r-i];
        cout << "d1[l+r-i] = " << d1[l+r-i] << " =" << " r-i+1 = " <<  r-i+1 << "\n";
      }
    }
    while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) {
        k++;
    }
    d1[i] = k--;
    cout << "final k: " << k << "\n";
    if (i + k > r) {
        l = i - k;
        r = i + k;
    }

    for (auto let: d1){
    cout << let << " ";
  } cout << "\n";
  }


  for (auto let: d1){
    cout << let << " ";
  } cout << "\n";

  return 0;
}