#include <bits/stdc++.h>
using namespace std;
string players, prevv;
int a = 0;
bool good = false;

int main(){
    cin >> players;

    prevv = to_string(players[0]); a++;
    for (int i= 1; i < players.size(); i++){
        if (to_string(players[i]) == prevv){
            a++;
        } else {
            a = 1;
            prevv = to_string(players[i]);
        }
        if (a == 7){
            good = true;
            break;
        }
    }
    if (good){
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}