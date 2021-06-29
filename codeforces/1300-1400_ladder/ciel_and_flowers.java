import java.io.*;
import java.util.*;

public class ciel_and_flowers {
  static int r, g, b, t1, t2, t3;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    r = sc.readInt();
    g = sc.readInt();
    b = sc.readInt();

    t1 = calc(r, g, b, 0);
    t2 = calc(r, g, b, 1);
    t3 = calc(r, g, b, 2);
    
    System.out.println(Math.max(t1, Math.max(t2, t3)));  
  }

  public static int calc(int rr, int gg, int bb, int mix){
    int total = 0;
    total += mix;
    rr -= mix;
    gg -= mix;
    bb -= mix;
    
    total += rr/3;
    total += gg/3;
    total += bb/3;
    return (rr < 0 || gg < 0 || bb < 0) ? 0 : total;
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