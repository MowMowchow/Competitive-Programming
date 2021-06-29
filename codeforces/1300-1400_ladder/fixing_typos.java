import java.io.*;
import java.util.*;

public class fixing_typos {
  static String s, out = "";
  static int n, nn;
  static boolean skip = false;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    s = sc.readLine();
    n = s.length();
    
    for (int i = 0; i < n; i++){
      skip = false;
      nn = out.length();
      if (nn > 1){
        if (out.charAt(nn-2) == out.charAt(nn-1) && out.charAt(nn-1) == s.charAt(i)){
          skip = true;
        }
      }
      if (nn > 2){
        if (out.charAt(nn-3) == out.charAt(nn-2) && out.charAt(nn-1) == s.charAt(i)){
          skip = true;
        }
      }
      
      if (!skip) out += s.charAt(i);
    }
    System.out.println(out);
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