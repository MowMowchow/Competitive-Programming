#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pi;
int n, m, d, best;
vector<pi> foradj[500010];
vector<pi> backadj[500010];
int there[500010];
int back[500010];
const int BIGGIE = 999999999;

void spfa1(int start) {
    bool visited[500010] = {false};
    queue<int> queue; queue.push(start);
    there[start] = 0;

    while (!queue.empty()){
        int curr = queue.front(); queue.pop();
        visited[curr] = false;

        for (auto node: foradj[curr]){
            if (there[node.first] > there[curr] + node.second){
                there[node.first] = there[curr] + node.second;
                if (!visited[node.first]){
                    visited[node.first] = true;
                    queue.push(node.first);
                }
            }
        }
    }
}

void spfa2(int start) {
    bool visited[500010] = {false};
    queue<int> queue; queue.push(start);
    back[start] = 0;

    while (!queue.empty()){
        int curr = queue.front(); queue.pop();
        visited[curr] = false;

        for (auto node: backadj[curr]){
            if (back[node.first] > back[curr] + node.second){
                back[node.first] = back[curr] + node.second;
                if (!visited[node.first]){
                    visited[node.first] = true;
                    queue.push(node.first);
                }
            }
        }
    }
}


int main() {
    cin >> n >> m;

    for (int i = 1; i < n+1; i++){
        there[i] = BIGGIE;
        back[i] = BIGGIE;
    }

    for (int i = 0; i < m; i++){
        int a, b, k; cin >> a >> b >> k;
        foradj[a].push_back({b, k});
        backadj[b].push_back({a, k});
    }

    spfa1(1);
    spfa2(n);
    cin >> d;

    best = BIGGIE;
    for (int i = 0; i < d; i++){
        int a, b, k; cin >> a >> b >> k;
        best = min(best, there[a] + k + back[b]);
    }


    if (best == BIGGIE){
        cout << -1;
    }
    else{
        cout << best;
    }

    return 0;
}
