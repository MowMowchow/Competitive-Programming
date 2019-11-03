#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int n, curr = INT_MAX, nums[101];

int gcd(int a, int b){
    if (b==0){
        return a;
    }
    return gcd(b, a%b);
}

int main() {
    cin >> n;

    for (int i = 0; i < n; ++i){
        cin >> nums[i];
    }
    sort(nums, nums+n);

    for (int i = 0; i < n-1; ++i){
        if (i==0){
            curr = nums[1]-nums[0];
        }
        else{
            curr = gcd(curr, nums[i+1]-nums[i]);
        }
    }

    for (int i = 2; i <= curr/2; ++i){
        if (curr%i == 0){
            cout << i << " ";
        }
    }
    cout << curr << "\n";
}