#include <bits/stdc++.h>
using namespace std;
using ip = pair<int, int>;
int N, h, m, total = 1, tt = 1;
map<ip, bool> times;


int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> h >> m;
        ip temp = make_pair(h, m);
        if (times.find(temp) == times.end()){
            times[temp] = true;
            tt = 1;
        } else {
            tt++;
        }
        total = max(total, tt);
    }
    cout << total << "\n";

    return 0;
}