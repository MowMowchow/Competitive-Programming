#include <bits/stdc++.h>
using namespace std;
int foxes[100010], N, T, f, d, oadd = 0;
vector<int> guilty;


int main(){
    memset(foxes, 0, sizeof(0));
    cin >> N >> T;
    for (int i = 1; i <= N; i++){
        cin >> f >> d;
        if (d == -1){
            foxes[f]--;
            oadd++;
        } else {
            foxes[d]++;
        }
    }

    for (int i = 1; i <= N; i++){
        foxes[i] += oadd;
    }

    for (int i = 1; i <= N; i++){
        if (foxes[i] == T){
            guilty.push_back(i);
        }
    }

    if (!guilty.empty()){
        for (auto fox: guilty){
            cout << fox << " ";
        } cout << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}