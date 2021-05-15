import java.io.*;
import java.util.*;

public class counting_kangaroos_is_fun {
  static int arr[], n, end;
  static boolean hit[];

  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    n = sc.readInt();
    arr = new int[n];
    hit = new boolean[n];
    for (int i = 0; i < n; i++) arr[i] = sc.readInt();

    Arrays.sort(arr); 

    end = n/2;
    int j = 0;
    while (j < n/2){
      if (arr[j]*2 > arr[end]) end++;
      else if (arr[j]*2 <= arr[end]){ j++; end++;}
      if (end >= n) break;
    }
    System.out.println(n-j);
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