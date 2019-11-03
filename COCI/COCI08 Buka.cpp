#include <iostream>
#include <string>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
long long total = 0;
string thing, a, b, big, small;
int main() {
    cin >> a >> thing >> b;
    if (a.size() > b.size()){
        big = a;
        small = b;
        //cout << big << " " << small << "\n";
    }
    else if (a.size() < b.size()){
        big = b;
        small = a;
    }
    else{
        big = a;
        small = b;
    }

    if (thing == "+"){
        //cout << "1";
        for (int i = big.size(); i > 0; i--){
            if (i == small.size()){
                if (i == big.size()){
                    cout << "2";
                }
                else {
                    cout << "1";
                }
            }
            else if (i == big.size()){ // fix
                cout << "1";
            }
            else{
                cout << "0";
            }
        }
    }
    else if (thing == "*"){
        cout << "1";
        total = a.size() + b.size() - 1;
        for (int i = 1; i < total; i++){
            cout << "0";
        }
    }
    else{
        cout << "uh";
    }

}
