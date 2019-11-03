#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
const int BIGGIE = 99999999;
int n, m, skyscrapers[30010], x, y, b, p;
set<int> powers[30010];


void spfa(){
    int curr, jumps, d;
    queue<vector<int> > queue; queue.push({x, 0});
    vector<int> temp;
    skyscrapers[x] = 0;

    while (!queue.empty()){
        temp = queue.front(), queue.pop();
        curr = temp[0]; d = temp[1];
        if (d <= skyscrapers[curr]) {
            for (auto dogepwr: powers[curr]) {
                jumps = 1;
                for (int spot = curr + dogepwr; spot < n; spot += dogepwr) {
                    if (skyscrapers[spot] > skyscrapers[curr] + jumps) {
                        skyscrapers[spot] = skyscrapers[curr] + jumps;
                        queue.push({spot, skyscrapers[spot]});
                        if (powers[spot].count(dogepwr)){
                            break;
                        }
                    }
                    jumps++;
                }
                jumps = 1;
                for (int spot = curr - dogepwr; spot >= 0; spot -= dogepwr) {
                    if (skyscrapers[spot] > skyscrapers[curr] + jumps) {
                        skyscrapers[spot] = skyscrapers[curr] + jumps;
                        queue.push({spot, skyscrapers[spot]});
                        if (powers[spot].count(dogepwr)){
                            break;
                        }
                    }
                    jumps++;
                }
            }
        }
    }
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++){
        cin >> b >> p;
        if (i == 0){
            x = b;}
        else if (i == 1){
            y = b;}
        powers[b].insert(p);
    }

    fill(skyscrapers, skyscrapers+n+5, BIGGIE);
    spfa();

    if (skyscrapers[y] == BIGGIE){
        cout << "-1\n";
    }
    else{
        cout << skyscrapers[y] << "\n";
    }
    return 0;
}