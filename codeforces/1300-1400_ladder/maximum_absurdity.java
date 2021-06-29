import java.io.*;
import java.util.*;

public class maximum_absurdity {
  static int n, k;
  static long arr[], og[], out[], maxleft[][], maxright[][], curr = 0;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    n = sc.readInt();
    k = sc.readInt();
    og = new long[n+2]; og[n+1] = 0;
    arr = new long[n+1-k];
    maxleft = new long[n+1-k][2];
    maxright = new long[n+1-k][2];
    for (int i = 1; i <= n; i++) og[i] = sc.readInt();

    for (int i = n-1; i >= 0; i--){
      if (i > n-k) curr += og[i+1];
      else {
        curr += og[i+1]-og[i+k+1];
        arr[i] = curr;
      }
    }

    maxleft[0][0] = arr[0]; maxleft[0][1] = 0;
    for (int i = 1; i <= n-k; i++){
      if (arr[i] > maxleft[i-1][0]){
        maxleft[i][0] = arr[i];
        maxleft[i][1] = i;
      } else {
        maxleft[i][0] = maxleft[i-1][0];
        maxleft[i][1] = maxleft[i-1][1];
      }
    }
    maxright[n-k][0] = arr[n-k]; maxright[n-k][1] = n-k;
    for (int i = n-k-1; i >= 0; i--){
      if (arr[i] >= maxright[i+1][0]){
        maxright[i][0] = arr[i];
        maxright[i][1] = i;
      } else {
        maxright[i][0] = maxright[i+1][0];
        maxright[i][1] = maxright[i+1][1];
      }
    }

    out = new long[3];
    for (int i = 0; i <= n-(2*k); i++){
      if (maxleft[i][0] + maxright[i+k][0] > out[0]){
        out[0] = maxleft[i][0] + maxright[i+k][0];
        out[1] = maxleft[i][1];
        out[2] = maxright[i+k][1];
      }
    }
    System.out.println((out[1]+1) + " " + (out[2]+1));
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