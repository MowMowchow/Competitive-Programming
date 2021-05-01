import java.io.*;
import java.util.*;

public class fox_dividing_cheese{
  static int a, b, p, q, x1, x2, y1, y2, z1, z2;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    a = sc.readInt(); b = sc.readInt();

    while (a % 2 == 0){
      a /= 2;
      x1++;      
    }
    while (b % 2 == 0){
      b /= 2;
      x2++;      
    }
    while (a % 3 == 0){
      a /= 3;
      y1++;      
    }
    while (b % 3 == 0){
      b /= 3;
      y2++;      
    }
    while (a % 5 == 0){
      a /= 5;
      z1++;      
    }
    while (b % 5 == 0){
      b /= 5;
      z2++;      
    }

    if (a == b){
      System.out.println(Math.abs(x1-x2)+Math.abs(y1-y2)+Math.abs(z1-z2));
    } else System.out.println(-1);
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