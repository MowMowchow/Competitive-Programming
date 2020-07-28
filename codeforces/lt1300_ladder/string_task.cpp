#include <bits/stdc++.h>
using namespace std;
string s, a = "";
int n;


int main(){
    cin >> s;
    n = s.size();

    for (auto let: s){
        if (toupper(let) == 'A' || toupper(let) == 'O' || toupper(let) == 'Y' || toupper(let) == 'E' || toupper(let) == 'U' || toupper(let) == 'I'){
            continue;
        } else {
            a += let;
        }
    } s = a; a = "";
    for (auto let: s){
        a += tolower(let);
    } s = a; a = "";
    for (auto let: s){
        a += '.'; a += let;
    }
    cout << a << "\n";
    return 0;
}