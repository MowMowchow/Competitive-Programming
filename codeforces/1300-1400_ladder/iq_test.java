import java.io.*;
import java.util.*;

public class iq_test{
  static char grid[][];
  static boolean out = false;
  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    grid = new char[5][5];
    for (int i = 1; i <= 4; i++){
      String temp = sc.readLine();
      for (int j = 1; j <= 4; j++){
        grid[i][j] = temp.charAt(j-1);
      }
    }
    
    for (int i = 1; i < 4; i++){
      for (int j = 1; j < 4; j++){
        int hash = 0, dot = 0;
        if (grid[i][j] == '#') { 
          hash++;
        } else { dot ++; }
        
        if (grid[i+1][j+1] == '#') { 
          hash++;
        } else { dot ++; }
        
        if (grid[i+1][j] == '#') { 
          hash++;
        } else { dot ++; }
        
        if (grid[i][j+1] == '#') { 
          hash++;
        } else { dot ++; }
        
        if (hash == 4 || dot == 4 || hash == 3 || dot == 3){out = true;}
        
      }
    }
    System.out.println(out ? "YES" : "NO");
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