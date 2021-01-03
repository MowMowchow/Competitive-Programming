#include <bits/stdc++.h>
using namespace std;
int n, x, arr[200000];


int binsearch(int goal, int length){
  int l = 0, r = length-1, mid;
  while (l < r){
    mid = l+(r-l+1)/2;
    if (arr[mid] == goal){
      return mid;
    }
    else if (arr[mid] < goal){
      l = mid;
    } else {
      r = mid-1;
    }
  }
  return l;
}


int main(){
  cin >> n;
  for (int i = 0; i < n; i++){
    cin >> arr[i];
  }
  cin >> x;

  cout << binsearch(x, n) << "\n";
  return 0;
}