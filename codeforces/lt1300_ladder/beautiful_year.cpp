#include <bits/stdc++.h>
using namespace std;
int n;
map<string, bool> vis;
string nstr;

int main(){
    cin >> n;
    n++;

    while (true){
        nstr = to_string(n);
        bool done = true;

        for (int i = 0; i < 4; i++){
            if (vis.find(to_string(nstr[i])) == vis.end()){
                vis[to_string(nstr[i])] = true;
            } else {

                done = false;}
        }

        if (done){
            break;
        } else {
            n++;
            vis.clear();
        }


    }
    cout << n << "\n";

    return 0;
}