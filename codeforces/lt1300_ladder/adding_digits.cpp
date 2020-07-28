#include <bits/stdc++.h>
using namespace std;
bool good = false;
int a, b, n;
string s;


int main(){
    cin >> a >> b >> n;

    a *= 10;
    for (int j = 0; j < 10; j++){
        if (a % b == 0){
            good = true;
            break;
        }
        a++;
    }

    if (!good){cout << -1 << "\n";}
    else{
        n--;
        s = to_string(a);
        s += string(n, '0');
        cout << s << "\n";
    }    
    return 0;
}