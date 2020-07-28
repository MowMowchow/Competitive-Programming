#include <bits/stdc++.h>
using namespace std;

map<__CHAR32_TYPE__, int> letters;
string og, out = "";
int k, prevv, c = 0;
bool good = true;
int main(){
    
    cin >> k >> og;

    for (auto letter: og){
        if (letters.find(letter) == letters.end()){
            letters[letter] = 1;
        } else {
            letters[letter] += 1;

        }
    }

    
    for (auto item: letters) {
        if (item.second%k != 0){
            good = false;
        }
    }

    if (good){
        for (auto item: letters) {
            out += string((item.second/k), item.first);
        }
        for (int i = 0; i < k; i++){
            cout << out;
        }cout << "\n";
    } else {
        cout << -1 << "\n";
    }


    return 0;
}