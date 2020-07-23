#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int H, N, X, Y, nw[1010], na[1010], a[1010][110][2], nt[1010], dp[1010][2], ndp[1010][110][110];
// a = for each node -> achievements -> time, point
// nw = node weight | na = node achievements
// nt = node time  | dp[i][0/1] = max val at node i, time spent at node
// ndp = knapsack for each node
vector<int> adj[1010];


void solve(int p){
    //cout << "hello\n";
    cout << "p: "  << p << " na[p]: " << na[p] << " | nt[p]: " << nt[p]  << " | nw[p]: " << nw[p] << "\n";

    for (int i = 1; i <= na[p]; i++){  // num of achievements
        for (int j = 1; j <= nt[p]; j++){  // time able to spend at node
            if (j >= a[p][i][0]){
                ndp[p][i][j] = max(ndp[p][i-1][j], ndp[p][i-1][j-a[p][i][0]] + a[p][i][1]);}
            else{
                ndp[p][i][j] = ndp[p][i-1][j];}
        }
    }

    for (int i = 0; i <= na[p]; i++){  // num of achievements
        cout << "DOING ACHIEVEMENT I: " << i << "\n";
        for (int j = 0; j <= nt[p]; j++){  // time able to spend at node
            cout << "time: " << j << " | " << ndp[p][i][j] << " ";
        }cout << "\n";
    }
    cout << "\n";
}


int dfs(int curr, int prev, int tl, int currp){ // tl = timeleft,
    tl -= nw[curr];
    int temp = 0;

    for (int temptl = min(tl, nt[curr]); temptl >= 0; temptl--){ // temptl = time spent on curr
        temp = max(temp, currp+ndp[curr][na[curr]][temptl]);
        int res = 0, ttlnodet = 0;
        //cout << "TEMP: " << temp << " | AT NODE: " << curr << " | TEMPTL: " << temptl << " | CURRTL: " << tl << " | NT[CURR]: " << nt[curr] << " | NW[CURR]: " << nw[curr] << " | ADDED: " << ndp[curr][na[curr]][temptl] << "\n";
        for (auto node: adj[curr]) {
            if (node != prev){
                if (tl-temptl-ttlnodet-nw[node] >= 0) {
                    ttlnodet += nw[node];
                    //cout << "NOW GOING TO: " << node << "\n";
                    res +=  dfs(node, curr, tl-temptl-ttlnodet-nw[node], currp + ndp[curr][na[curr]][temptl]);
                }
            }
        }
    }
    return temp;
}



int main() {
    memset(nt, 0, sizeof(nt));
    memset(na, 0, sizeof(na));
    memset(nw, 0, sizeof(nw));
    memset(dp, 0, sizeof(dp));
    memset(ndp, 0, sizeof(ndp));

    cin >> H >> N;

    for (int i = 1; i <= N; i++){
        cin >> nt[i] >> na[i] >> nw[i];
        for (int j = 1; j <= na[i]; j++){
            cin >> a[i][j][0] >> a[i][j][1];
        }
        if (ndp[i][na[i]][nt[i]] == 0){
            solve(i);}
    }

    for (int i = 1; i < N; i++){
        cin >> X >> Y; ++X; ++Y;
        adj[X].push_back(Y);
        adj[Y].push_back(X);
    }

    int final = dfs(1, 0, H, 0);
    cout << final << "\n";

    return 0;
}