#include <bits/stdc++.h>
using namespace std;

int n, x, y, total = 0;
vector<vector<int>> bottles;
map<int, vector<int>> bm;
 
int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> x >> y;
        bottles.push_back({x, i+1});
        if (bm.find(y) == bm.end()){
            bm[y] = {i+1};
        } else {
            bm[y].push_back(i+1);
        }
    }   
 
    for (int i = 0; i < n; i++){
        vector<int> bottle = bottles[i];
        if (bm.find(bottle[0]) != bm.end()){
            for (auto index: bm[bottle[0]]){
                if (index != bottle[1]){
                    total++;
                    break;
                }
            }
        }

    }
    cout << n-total << "\n";
    return 0;
}