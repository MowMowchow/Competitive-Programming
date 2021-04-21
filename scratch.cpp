#include <bits/stdc++.h>
using namespace std;
int houses[100010], a[10010], b[10010], s[10010], sum = 0;

int main(){
    int N,L,S;
    cin >> N >> L >> S;

    memset(houses, 0, sizeof(houses));
    
    for (int i = 0; i<N; i++){
        cin >> a[i] >> b[i] >> s[i];
        for (int j = a[i]-1; j<b[i]; j++){
            houses[j] += s[i];
        }
    }    
    for (int i=0; i < L; i++){
        if (houses[i] < S){
            sum++;
        }
    }
    cout << sum;
}