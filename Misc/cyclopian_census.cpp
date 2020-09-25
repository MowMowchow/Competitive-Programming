#include <bits/stdc++.h>
using namespace std;

int N, Q, temp;
vector<int> ages;

int main(){
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> temp;
    ages.push_back(temp);
  }

  sort(ages.begin(), ages.end());

  cin >> Q;
  for (int i = 0; i < Q; i++){
    cin >> temp;
    cout << ages[temp-1] << "\n";
  } cout << "\n";

  return 0;
}