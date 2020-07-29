#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll x, y, n, seq[10];

int main(){
    memset(seq, 0, sizeof(seq));
    cin >> seq[1] >> seq[2] >> n;
    seq[1] += (ll)(pow(10, 9) + 7);
    seq[1] %= (ll)(pow(10, 9) + 7);
    seq[2] += (ll)(pow(10, 9) + 7);
    seq[2] %= (ll)(pow(10, 9) + 7);
    for (int i = 3; i <= 6; i++){
        seq[i] = seq[i-1]-seq[i-2];
        seq[i] += (ll)(pow(10, 9) + 7);
        seq[i] %= (ll)(pow(10, 9) + 7);
    }

    n %= 6;
    if (n == 0){
        n = 6;
    }
    cout << seq[n] << "\n";
    return 0;
}