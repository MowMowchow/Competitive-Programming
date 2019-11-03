#include <algorithm>
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
int n, a, b, citynum = 0, parsubsets[100010], ranksubsets[100010];

string x, aa, bb;
unordered_map<string, int> cities;

int find(int node){
    if (parsubsets[node] != node){
        return find(parsubsets[node]);
    }
    return parsubsets[node];
}

void unionn(int u, int v){
    if (ranksubsets[u] > ranksubsets[v]) {
        parsubsets[v] = parsubsets[u];
    }
    else if (ranksubsets[u] < ranksubsets[v]) {
        parsubsets[u] = parsubsets[v];
    }
    else {
        ranksubsets[u]++;
        parsubsets[v] = parsubsets[u];
    }
}

int donumber(string city){
    if (cities.find(city) == cities.end()){
        cities[city] = citynum;
        return citynum++;
    }
    return cities[city];
}

void clearr(){
    for (int i = 0; i < 100010; i++){
        parsubsets[i] = i;
    }
}



int main() {
    cin.sync_with_stdio(0);
    cin.tie(0);
    for (int i = 0; i < 100010; i++){
        parsubsets[i] = i;
    }
    for (int i = 0; i < 5; i++) {
        cin >> n;
        for (int q = 0; q < n; q++){
            cin >> x >> aa >> bb;
            a = donumber(aa);
            b = donumber(bb);
            if (x == "p"){
                unionn(find(a), find(b));
            }
            else{
                if (find(a) == find(b)){
                    cout << "connected\n";
                }
                else{
                    cout << "not connected\n";
                }
            }
        }
        cities.clear();
        clearr();
        citynum = 0;
    }
    return 0;
}
