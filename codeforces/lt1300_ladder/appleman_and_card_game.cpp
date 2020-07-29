#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll n, k;
ll total;
string seq;
map<string, ll> letmap;
vector<ll> amts;
vector<ll> fin;

int main(){
    cin >> n >> k >> seq;

    for (auto let: seq){
        if (letmap.find(to_string(let)) == letmap.end()){
            letmap[to_string(let)] = 1;
        } else {
            letmap[to_string(let)]++;
        }
    }

    for (auto item: letmap){
        amts.push_back(item.second);
    }

    sort(amts.begin(), amts.begin()+amts.size());

    for (int i = amts.size()-1; i >= 0; i--){
        if (k == 0){
            break;
        } else if (amts[i] > k) {
            fin.push_back(k); k -= k;
        } else {
            fin.push_back(amts[i]); k -= amts[i];
        }
    }

    for (auto num: fin){
        total += num*num;
    }
    cout << total << "\n";

    return 0;
}