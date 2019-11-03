#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int n, k, w, t, pins[10510], psa[10510], dp[10510][510];


int doo(int i, int j){ // i = current position, j = balls left
    if (i < 0 || j <= 0){
        return 0;
    }
    else if (dp[i][j] == -1){
        int currbowlval = 0, ind;
        if (i >= w-1){
            ind = i-w;
            currbowlval = psa[i]-psa[ind];
        }
        else{
            ind = 0;
            currbowlval = psa[i]-psa[ind];
        }
        currbowlval = psa[i]-psa[ind];
        dp[i][j] = max(doo(i-1, j), doo(ind, j-1) + currbowlval);
        if (j > 1){
            int pinsum = 0;
            for (int x = ind; x >= ind-w+1 && x > 0; x--){
                pinsum += pins[x];
                dp[i][j] = max(dp[i][j], doo(x-1, j-2) + pinsum + currbowlval);
            }
        }
    }
    return dp[i][j];
}


void run(){
    memset(psa, 0, sizeof(psa));
    memset(pins, 0, sizeof(pins));
    memset(dp, -1, sizeof(dp));
    cin >> n >> k >> w;
    for (int i = 1; i < n+1; i++){
        cin >> pins[i];
    }
    for (int i = 1; i < n+w+5; i++){
        psa[i] += psa[i-1] + pins[i];
    }
    int result;
    result = doo(n+w, k);
    cout << result << "\n";
}


int main() {
    cin >> t;
    for (int ttttttt = 0; ttttttt < t; ttttttt++){
        run();
    }
    return 0;
}