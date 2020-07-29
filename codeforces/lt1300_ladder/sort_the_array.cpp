#include <bits/stdc++.h>
using namespace std;
long long n, arr[100010], pre, changes, l, r = 0;
bool up, done = true;
vector<int> listt;

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }


    if (n == 1){
        cout << "yes\n" << 1 << " " << 1 << "\n";
    } else if (n == 2){
        if (arr[1] < arr[0]){
            cout << "yes\n" << 1 << " " << 2 << "\n";
        } else {
            cout << "yes\n" << 1 << " " << 1 << "\n";
        }
    } else if (n >= 3){
        if (arr[1] < arr[0]){ // start off as decrease
            up = false;
            changes = 1;
            l = 1;
        } else {
            up = true;
            changes = 0;
        }
        pre = arr[1];
        
        for (int i = 2; i < n; i++){
            if (arr[i] < pre && up){ // change to decrease
                up = false;
                changes++;
                l = i;
            } else if (arr[i] > pre && !up){ // change to increase
                up = true;
                changes++;
                r = i;
                
            }
            pre = arr[i];
        }
        if (changes == 1 && r == 0){
            r = n;
        }
        for (int i = 0; i < n; i++){
            if (l <= i+1 && i+1 <= r){
                listt.push_back(arr[r-((i+1)-l+1)]);
            }else {
                listt.push_back(arr[i]);
            }
        }
        for (int i = 1; i < n; i++){
            if (listt[i] <= listt[i-1]){
                done = false;
                break;
            }
        }
        if (changes == 2 && done){
        cout << "yes\n" << l << " " << r << "\n";
        } else if (changes == 1 && done) {
            cout << "yes\n" << l << " " << r << "\n";
        } else if (changes == 0){
            cout << "yes\n" << 1 << " " << 1 << "\n";
        } 
        else {
            cout << "no\n";
        }
    }
    return 0;
}