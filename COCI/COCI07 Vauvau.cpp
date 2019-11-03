#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;
int a, b, c, d, p, m, g, presult = 0, mresult = 0, gresult = 0, d1count = 0, d2count = 0;
bool d1mad = true, d2mad = true;

int main() {
    cin >> a >> b >> c >> d >> p >> m >>g;

    for (int i = 1; i < 1000; i++){
        if (d1mad && d1count == a){
            d1mad = false; d1count = 0;
        }
        else if (!d1mad && d1count == b){
            d1mad = true; d1count = 0;
        }
        if (d2mad && d2count == c){
            d2mad = false; d2count = 0;
        }
        else if (!d2mad && d2count == d){
            d2mad = true; d2count = 0;
        }


        if (d1mad && i == p){
            presult++;
        }
        if (d2mad && i == p){
            presult++;
        }
        if (d1mad && i == m){
            mresult++;
        }
        if (d2mad && i == m){
            mresult++;
        }
        if (d1mad && i == g){
            gresult++;
        }
        if (d2mad && i == g){
            gresult++;
        }



        d1count++; d2count++;
    }

    if (presult == 0){
        cout << "none\n";
    }
    else if (presult == 1){
        cout << "one\n";
    }
    else if (presult >= 2){
        cout << "both\n";
    }

    if (mresult == 0){
        cout << "none\n";
    }
    else if (mresult == 1){
        cout << "one\n";
    }
    else if (mresult >= 2){
        cout << "both\n";
    }

    if (gresult == 0){
        cout << "none\n";
    }
    else if (gresult == 1){
        cout << "one\n";
    }
    else if (gresult >= 2){
        cout << "both\n";
    }

    return 0;
}