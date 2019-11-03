#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define MAXN 100001

using namespace std;

int N, M, K, A, B;
bool giftbuildings[MAXN] = {false};
int totheshop[MAXN];
int tothefeast[MAXN];
vector<int> roads[MAXN];


void bfs(int a, bool there){
    bool visited[MAXN];
    fill_n(visited, MAXN, false);
    queue<vector<int> > queue;
    vector<int> newww; newww.push_back(a); newww.push_back(0);
    queue.push(newww);

    while (!queue.empty()){
        vector<int> curr = queue.front(); queue.pop();

        for (auto node: roads[curr[0]]){
            if (!visited[node]){
                visited[node] = true;
                vector<int> neww; neww.push_back(node); neww.push_back(curr[1]+1);
                queue.push(neww);

                if (giftbuildings[node]){
                    if (there){
                        totheshop[node] = min(totheshop[node], neww[1]);
                    }
                    else {
                        tothefeast[node] = min(tothefeast[node], neww[1]);
                    }
                }
            }
        }
    }
}


int main() {
    cin >> N >> M >> K >> A >> B;
    for (int i = 0; i < K; i++){
        int j; cin >> j;
        giftbuildings[j] = true;
    }
    for (int i = 0; i < M; i++){
        int a, b; cin >> a >> b;
        roads[a].push_back(b);
        roads[b].push_back(a);
    }
    fill_n(totheshop, MAXN, 1000001);
    fill_n(tothefeast, MAXN, 1000001);

    bfs(A, true);
    bfs(B, false);
    int distance = 99999999;

    for (int i = 1; i <= M; i++){
        distance =  min(distance, totheshop[i]+tothefeast[i]);

    }

    cout << distance;

    return 0;
}