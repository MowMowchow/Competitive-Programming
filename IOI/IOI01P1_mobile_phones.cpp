#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
int S, X, Y, A, L, B, R, T, BIT[1200][1200], type;

int sumBIT(int x, int y){
    int total = 0;
    for (int xx = x; xx > 0; xx -= (xx & -xx)){
        for (int yy = y; yy > 0; yy -= (yy & - yy)){
            total += BIT[xx][yy];
        }
    }
    return total;
}

void updateBIT(int x, int y, int k){
    for (int xx = x; xx <= S; xx += (xx & -xx)){
        for (int yy = y; yy <= S; yy += (yy & -yy)){
            BIT[xx][yy] += k;
        }
    }
}

void constructBIT(){
    for (int i = 0; i <= S; i++){
        for (int j = 0; j <= S; j++){
            BIT[i][j] = 0;
        }
    }
}

int query(int x1, int y1, int x2, int y2){ // L B R T
    int t1, t2, t3, t4, t5;
    t1 = sumBIT(x2, y2); // top corner
    t2 = sumBIT(x2, y1-1); // bottom side
    t3 = sumBIT(x1-1, y1-1); // diagonal rectangle
    t4 = sumBIT(x1-1, y2); // left rectangle
    t5 = t1-t2-t4+t3;
    return t5;
}


int main() {
    while (true){
        cin >> type;
        if (type == 0){
            cin >> S;
            constructBIT();
        }
        else if (type == 1){
            cin >> X >> Y >> A;
            updateBIT(X+1, Y+1, A);
        }
        else if (type == 2){
            cin >> L >> B >> R >> T;
            int res;
            res = query(L+1, B+1, R+1, T+1);
            cout << res << "\n";
        }
        else if (type == 3){
            break;
        }
        else{
            cout << "what\n";
        }

    }
    return 0;
}