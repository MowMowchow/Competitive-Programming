import java.io.*;
import java.util.*;

public class insomnia_cure {
  static int arr[], k, l, m, n, d, curr, total;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    k = sc.readInt();
    l = sc.readInt();
    m = sc.readInt();
    n = sc.readInt();
    d = sc.readInt();
    arr = new int[d+10]; 

    curr = 1;
    while (curr*k <= d){
      if (arr[curr*k] == 0){
        arr[curr*k] = 1; total++;
      }
      curr++;
    }
    curr = 1;
    while (curr*l <= d){
      if (arr[curr*l] == 0){
        arr[curr*l] = 1; total++;
      }
      curr++;
    }
    curr = 1;
    while (curr*m <= d){
      if (arr[curr*m] == 0){
        arr[curr*m] = 1; total++;
      }
      curr++;
    }
    curr = 1;
    while (curr*n <= d){
      if (arr[curr*n] == 0){
        arr[curr*n] = 1; total++;
      }
      curr++;
    }
    System.out.println(total);
  }


  public static class FastIn {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    String next () throws IOException {
        while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(input.readLine().trim());
        return st.nextToken();
    }
    long readLong () throws IOException {
        return Long.parseLong(next());
    }
    int readInt () throws IOException {
        return Integer.parseInt(next());
    }
    double readDouble () throws IOException {
        return Double.parseDouble(next());
    }
    char readChar () throws IOException {
        return next().charAt(0);
    }
    // entire string
    String readLine () throws IOException {
        return input.readLine().trim();
    }
  }
}