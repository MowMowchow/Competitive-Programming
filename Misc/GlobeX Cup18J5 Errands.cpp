#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define MAXN 100001

using namespace std;
int n, m, q, c;
vector<int> adj[MAXN];
bool visited[MAXN] = {false};
int answers[MAXN];


int main() {
    cin >> n >> m >> q >> c;
    fill_n(answers, MAXN, MAXN);
    answers[c] = 0;
    for (int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);

    }

    queue<vector<int> > queue;
    vector<int> curr = {c, 0};
    queue.push(curr);
    while (!queue.empty()){
        vector<int> curr = queue.front(); queue.pop();
        if (!visited[curr[0]]) {
            visited[curr[0]] = true;
            for (auto node: adj[curr[0]]) {
                vector<int> neww = {node, curr[1] + 1};
                answers[node] = min(answers[node], neww[1]);
                queue.push(neww);
            }
        }
    }

    for (int i = 0; i < q; i++){
        int a, b; cin >> a >>b;
        //cout << answers[a] << " " << answers[b] << "\n";
        if (answers[a] == MAXN || answers[b] == MAXN){
            cout << "This is a scam!\n";
        }
        else{
            cout << answers[a]+answers[b] << "\n";
        }
    }
    return 0;
}