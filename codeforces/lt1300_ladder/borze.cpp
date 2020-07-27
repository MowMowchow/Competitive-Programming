#include <bits/stdc++.h>
using namespace std;
string str, out = "";
int n, i = 0;

int main() {
    cin >> str;
    n = str.length();

    while (i < n){
        if (i < n-1){
            if (str.substr(i, 2) == "-."){
                out += "1"; i += 2;
            } else if (str.substr(i, 2) == "--"){
                out += "2"; i += 2;
            } else {
                out += "0"; i++;
            }
        } else {
            out += "0"; i++;
        }
    }
    cout << out;
    return 0;
}