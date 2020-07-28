#include <bits/stdc++.h>
using namespace std;
int n, a, b;
// min a people in front of him
// max b people behind him

int main(){
    cin >> n >> a >> b;
    n -= a;
    b++;
    if (n >= b){
        cout << b << "\n";
    } else if (n < b){
        cout << n << "\n";
    }
    return 0;
}