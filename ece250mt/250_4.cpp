#include <iostream>

using namespace std;
int main(){
  ifstream fin("inputData.txt");
  char nextInput = 0; // assuming nextInput is the next char
  StackAsArray<char> stk;

  while (fin >> nextInput){
    if (nextInput == "("){
      stk.push(")");
    } else if (nextInput == "["){
      stk.push("]");
    } else {
      if (!stk.empty()){
        if (stk.top() != nextInput){
          cout << "invalid\n";
          break;
        } else {
          stk.pop();
        }
      }else{
        cout << "invalid\n";
        break;
      }
    }
  }
  cout << "valid\n";
  return 0;
}