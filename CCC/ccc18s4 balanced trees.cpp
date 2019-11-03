#include <bits/stdc++.h>
using namespace std;

#define MAXN ((int) 1e9 + 5)

int n, rooted;
long long dp1[(int) sqrt(MAXN) + 5], dp2[(int) sqrt(MAXN) + 5];


long long f(int w){
    if (w == 1){
        return 1LL;
    }
    long long &result = w <= rooted ? dp1[w] : dp2[n/w];
    if (result){
        return result;
    }
    int wsqrt = (int) sqrt(w);
    for (int j = 1; j <= wsqrt; j++){
        result += f(j)*(w/j - w/(j+1));

        if (j >= 2 && w/j > wsqrt){
            result += f(w/j);
        }
    }
    return result;
}


int main() {
    cin >> n;
    memset(dp1, 0, sizeof(dp1));
    memset(dp2, 0, sizeof(dp2));
    rooted = (int) sqrt(n);
    cout << f(n);
    return 0;
}