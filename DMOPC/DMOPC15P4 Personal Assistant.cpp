#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define bigint long long
using namespace std;

bigint n, dp[100010], temp, r, l, h;
vector<vector<bigint> > animes;

bigint binsearch(bigint goal){
    bigint left = 0, right = n-1, ind = 0;
    while (left < right){
        ind = left+(right-left+1)/2;

        if (animes[ind][0] <= goal){
            left = ind;
        }
        else{
            right = ind-1;
        }
    }
    return left;
}


int main() {
    animes.push_back({0, 0, 0});
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> r >> l >> h;
        animes.push_back({r+l-1, r, h});
    }
    sort(animes.begin(), animes.end()); // finish, release, happiness
    dp[1] = animes[1][2];
    for (int i = 2; i <= n; i++){
        temp = binsearch(animes[i][1]-1);

        if (temp >= 0){
            dp[i] = max(dp[i-1], dp[temp] + animes[i][2]);
        }
        else{
            dp[i] = max(dp[i-1], animes[i][2]);
        }
    }
    cout << dp[n] << "\n";
    return 0;
}
