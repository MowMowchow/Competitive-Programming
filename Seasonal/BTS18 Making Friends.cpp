#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define ll long long
using namespace std;
ll n, x, temp, curr, total, zero = 0;
vector<ll> calls;


int main() {
    cin >> n >> x;
    for (int i = 0; i < n; i++){
        cin >> temp; calls.push_back(temp);
    }
    sort(calls.rbegin(), calls.rend());

    curr = 0;
    while (x > 0) {
        if (curr == n-1){ // reaching the end
            total += max(calls[curr], zero);
            calls[curr]--;
            x--;
            curr--;
        }
        else if (curr > 0 && calls[curr] < calls[curr-1]){ // curr is less than left
            curr--;
        }
        else if (calls[curr] > calls[curr+1]){ // curr is greater than right
            total += max(calls[curr], zero);
            calls[curr]--;
            x--;

        }
        else if (calls[curr] == calls[curr+1]){ // curr is equal to right
            curr++;
        }
        else if (calls[curr] < calls[curr+1]){
            curr++;
        }
    }
    cout << total << "\n";
    return 0;
}