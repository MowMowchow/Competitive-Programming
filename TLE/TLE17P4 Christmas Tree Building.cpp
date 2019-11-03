#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define ll long long
using namespace std;
ll n, m, q, a, b, c, center[3] = {9999999999999, 0, 0}; // length, root, depth?
vector<vector<ll> > adj[100010];
bool uncounted[100010];
ll dists[100010];
ll paths[100010];

void dfs(ll curr, ll prev, ll length, ll &root, ll &dia){
    uncounted[curr] = true;
    paths[curr] = prev;
    if (length > dia){
        dia = length;
        root = curr;
    }
    for (auto temp: adj[curr]){
        ll node = temp[0], weight = temp[1];
        if (node != prev){
            dists[node] = weight;
            dfs(node, curr, length+weight, root, dia);
        }
    }
}

int main() {
    cin >> n >> m >> q;
    for (int i = 0; i < m; i++){
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }

    memset(uncounted, false, sizeof(uncounted));
    memset(paths, -1, sizeof(paths));

    if (q == 1){
        ll maxdiam = 0, counted = 0;
        for (int i = 1; i <= n; i++){
            if (!uncounted[i]){
                ll rootnode = i, rootdia = 0;
                dfs(i, i, 0, rootnode, rootdia);
                rootdia = 0;
                dfs(rootnode, 0, 0, rootnode, rootdia);
                counted++;
                maxdiam += rootdia;
            }
        }
        cout << (maxdiam + counted - 1) << "\n";
    }

    else if (q == 2){
        ll maxradius = 0;
        for (int i = 1; i <= n; i++){
            if (paths[i] == -1){
                ll rootnode = i, rootdia = 0;

                dfs(i, i, 0, rootnode, rootdia);
                rootdia = 0;
                dfs(rootnode, rootnode, 0, rootnode, rootdia);

                ll currradius = rootdia, currtotal = 0;
                for (int j = rootnode; j != paths[j]; j = paths[j]){
                    currradius = min(currradius, max(currtotal, rootdia-currtotal));
                    currtotal += dists[j];
                }
                if (currradius == maxradius){
                    currradius++;
                }
                maxradius = max(maxradius, currradius);

            }
        }
        cout << maxradius << "\n";
    }

    return 0;
}