#include <iostream>
using namespace std;

int main() {
  int q = 0; cin >> q;
  int reactions[5][4] = {
    {2, 1, 0, 2},
    {1, 1, 1, 1},
    {0, 0, 2, 1},
    {0, 3, 0, 0},
    {1, 0, 0, 1}
  };
  bool dp[31][31][31][31] = {{{{false}}}};

  for (int a = 0; a <= 30; a++){
    for (int b = 0; b <= 30; b++){
      for (int c = 0; c <= 30; c++){
        for (int d = 0; d <= 30; d++){
          for (int r = 0; r < 5; r++){
            if (a >= reactions[r][0] && b >= reactions[r][1] && c >= reactions[r][2] && d >= reactions[r][3]){
              if (!dp[a-reactions[r][0]][b-reactions[r][1]][c-reactions[r][2]][d-reactions[r][3]]){
                dp[a][b][c][d] = true;
              }
            }
          }
        }
      }
    }
  }


  for (int i = 0; i < q; i++){
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    if (dp[A][B][C][D]){
      cout << "Patrick" << "\n";
    }
    else{
      cout << "Roland" << "\n";
    }
  }

}