#include <bits/stdc++.h>
using namespace std;
 
int arr[60], temp[60], N, T;
string a;
int main(){
    cin >> N >> T >> a;
    for (int i = 0; i < N; i++){
        if (a[i] == 'B'){arr[i] = 1;}
        else{arr[i] = 0;}
    }
 
    for (int t = 0; t < T; t++){
        int i = N-1;
        while (i >= 0){
            if (i > 0 && arr[i] == 0 && arr[i-1] == 1){ // 1 = boy
                temp[i] = 1; temp[i-1] = 0; i--;}
            else{temp[i] = arr[i];}
            i--;
        }
        for (int j = 0; j < N; j++){
            arr[j] = temp[j];
        }
    }
 
    for (int i = 0; i < N; i++){
        if (arr[i] == 1){cout << "B";}
        else{cout << "G";}
    }cout << "\n";
}