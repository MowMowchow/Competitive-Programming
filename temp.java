import java.io.*;
import java.util.*;

public class temp {
  static String a, b, c;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    a = sc.readLine();
    b = sc.readLine();
    c = sc.readLine();

    System.out.println(a + " " + b + " " + c);

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