#include <bits/stdc++.h>
using namespace std;
<<<<<<< HEAD
typedef long long ll;
typedef vector<int> vec1i;
typedef vector<vector<int>> vec2i;
typedef vector<vector<vector<int>>> vec3i;
typedef vector<ll> vec1ll;
typedef vector<vector<ll>> vec2ll;
typedef vector<vector<vector<ll>>> vec3ll;


int main(){
  cout << " hi \n";
  return 0;
=======
int houses[100010], a[10010], b[10010], s[10010], sum = 0;

int main(){
    int N,L,S;
    cin >> N >> L >> S;

    memset(houses, 0, sizeof(houses));
    
    for (int i = 0; i<N; i++){
        cin >> a[i] >> b[i] >> s[i];
        for (int j = a[i]-1; j<b[i]; j++){
            houses[j] += s[i];
        }
    }    
    for (int i=0; i < L; i++){
        if (houses[i] < S){
            sum++;
        }
    }
    cout << sum;
>>>>>>> ab75609ae003930f41031287ba9c578f1f33bcdc
}