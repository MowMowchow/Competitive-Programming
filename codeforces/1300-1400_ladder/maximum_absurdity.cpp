#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll N, K, l, r, total = 0, ind1, ind2, tempsize = 1, tempsum = 0;
ll a, b, arr[200010], maxleft[200010], maxright[200010];



int main(){
  cin >> N >> K;
  memset(maxleft, 0, sizeof(maxleft));
  memset(maxright, 0, sizeof(maxright));

  for (int i = 0; i < N; i++){
    cin >> arr[i];
  }

  l = 0; r = K;

  for (int i = 1; i <= N; i++){
    if (tempsize < K){
      tempsize++;
    } else {
      tempsum -= arr[i-K-1];
    }
    tempsum += arr[i-1];
    maxleft[i] = max(maxleft[i-1], tempsum);
  }

  tempsize = 0; tempsum = 0;
  for (int i = N-1; i >= 0; i++){
    if (tempsize < K){
      tempsize++;
    } else {
      tempsum -= arr[i+K];
    }
    tempsum += arr[i]; // fix this
    maxright[i] = max(maxright[i+1], tempsum);
  }

  for (int i = 0; i <= N; i++){
    cout << maxleft[i] << " ";
  
  }

  




  return 0;
}