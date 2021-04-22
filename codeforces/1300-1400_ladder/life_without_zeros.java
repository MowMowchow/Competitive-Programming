import java.io.*;
import java.util.*;

public class life_without_zeros {
  static String a, b, c, a_t = "", b_t = "", c_t = "";
  static int an, bn, cn, a_tn, b_tn, c_tn;
  static boolean out;
  
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    a = sc.readLine();
    b = sc.readLine();
    for (int i = 0; i < a.length(); i ++){
      if (a.charAt(i) != '0'){
        a_t += Character.toString(a.charAt(i));
       }
    }
    for (int i = 0; i < b.length(); i ++){
      if (b.charAt(i) != '0'){
        b_t += Character.toString(b.charAt(i));
      }
    }

    an = Integer.parseInt(a);
    bn = Integer.parseInt(b);
    cn = an+bn;
    c = Integer.toString(cn);
    
    for (int i = 0; i < c.length(); i ++){
      if (c.charAt(i) != '0'){
        c_t += Character.toString(c.charAt(i));
      }
    }

    a_tn = Integer.parseInt(a_t);
    b_tn = Integer.parseInt(b_t);
    c_tn = a_tn+b_tn;
    
    System.out.println(Integer.parseInt(c_t) == c_tn ? "YES" : "NO");
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