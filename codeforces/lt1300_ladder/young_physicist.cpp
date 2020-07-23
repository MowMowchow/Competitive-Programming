#include <bits/stdc++.h>
using namespace std;
int arr[110][3], N;
 
int main(){
     cin >> N;
 
     for (int i = 1; i <= N; i++){
         cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
         arr[i][0] += arr[i-1][0];
         arr[i][1] += arr[i-1][1];
         arr[i][2] += arr[i-1][2];}
 
     if (!arr[N][0] && !arr[N][1] && !arr[N][2]){
        cout << "YES";}
     else{
         cout << "NO";}
 
 
}