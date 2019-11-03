#include <bits/stdc++.h>
#include <iostream>
#include <vector>

#define MAXN 150001

using namespace std;

int N, M, Q;
int templines[MAXN];
int stations[MAXN];
int stationsBIT[MAXN];


int sumBIT(int k){
    int total = 0;
    while (k >= 1){
        total += stationsBIT[k];
        k -= k&-k;
    }
    return total;
}


void updateBIT(int k, int x){
    while (k <= N){
        stationsBIT[k] += x;
        k += k&-k;
    }
}


void operate(vector<vector<vector<int>>> &lines, int line){
    int n = lines[line].size();
    int firstind = lines[line][0][0];
    int oldind = lines[line][n-1][0];

    for (int i = n-1; i > -1; i--){
        if (i < n-1){
            int newval = lines[line][i][1] - lines[line][i+1][1];
            int updateind = oldind;
            oldind = lines[line][i][0];
            lines[line][i][0] = updateind;
            stations[updateind] = lines[line][i][1];

            updateBIT(updateind+1, newval);
        }

        else if (i == n-1){
            int newval = lines[line][i][1]-lines[line][0][1];
            lines[line][i][0] = firstind;
            stations[firstind] = lines[line][0][1];

            updateBIT(firstind+1, newval);
        }
    }
}


int main(){
    cin >> N >> M >> Q;
    vector<vector<vector<int>>> lines(M+1);
    lines[0].push_back({0});

    // input and defining
    for (int i = 0; i < N; i++){
        cin >> templines[i];
    }
    for (int i = 0; i < N; i++){
        cin >> stations[i];
    }

    for (int i = 0; i < N; i++){
        vector<int> temp{i, stations[i]};
        lines[templines[i]].push_back(temp);
    }

    // creating BIT
    for (int i = 1; i < N+1; i++){
        updateBIT(i, stations[i-1]);
    }

    // queries
    for (int q = 0; q < Q; q++){
        int op; cin >> op;
        if (op == 1) {
            int l, r;
            cin >> l >> r;
            //cout << "Operation 1 " << l << " " << r << "\n";
            cout << sumBIT(r) - sumBIT(l - 1) << "\n";
        }

        else if (op == 2){
            int x; cin >> x;
            //cout << "Operation 2 " << x << "\n";
            operate(lines, x);
        }

        //else{
        //    cout << "what";
        //}
    }


    return 0;
}