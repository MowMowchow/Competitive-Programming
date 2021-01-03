#include <bits/stdc++.h>
using namespace std;
int n, arr[200000], l, r, mid, x;


int main(){

  cin >> n;
  for (int i = 0; i < n; i++){
    cin >> arr[i];
  }
  cin >> x;
  l = 0; r = n-1;

  while (l < r){
    mid = l+(r-l+1)/2;

    if (arr[mid] == x){
      return mid
    }
    else if (arr[mid] < x){
      l = mid;
    } else {
      r = mid-1;
    }
  }
  
  cout << l << "\n";

  return 0;
}