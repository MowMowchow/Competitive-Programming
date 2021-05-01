import java.io.*;
import java.util.*;

public class dima_and_continuous_line{
  static int n, nums[];
  static boolean out = true;
  public static boolean check(int x_1, int x_3){
    int x_2 = x_1+1;
    int x_4 = x_3+1;
    return (nums[x_3] < nums[x_1] && nums[x_1] < nums[x_4] && nums[x_4] < nums[x_2]) || (nums[x_1] < nums[x_3] &&  nums[x_3] < nums[x_2] && nums[x_2] < nums[x_4]);
  }

  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    n = sc.readInt();
    
    nums = Arrays.stream(sc.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    
    for (int i = 0; i < n-1; i++){
      for (int j = 0; j < n-1; j++){
        out = check(i, j) ? false : out;
      }
    }
    System.out.println(!out ? "yes" : "no");
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