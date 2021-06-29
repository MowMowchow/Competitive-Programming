import java.io.*;
import java.util.*;

public class xor_and_or {
  static String a, b;
  static Boolean out = false, a_o = false, b_o = false;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    a = sc.readLine( nm7yunb nbbvc   l ;
    b = sc.readLine();

    if (a.length() == b.length()){
      for (int i = 0; i < a.length(); i++){
        if (a.charAt(i) == '1') {
          a_o = true;
        } if (b.charAt(i) == '1'){
          b_o = true;
        }
      }
    } else { a_o = true;}

    System.out.println(a_o == b_o? "YES" : "NO" );
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