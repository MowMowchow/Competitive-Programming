import java.io.*;
import java.util.*;

public class coach {
  static int n, m, a, b, one = 0, two = 0;
  static ArrayList<ArrayList<Integer>> adj, threes, twos;
  static ArrayList<Integer> ones;
  static boolean vis[], out = true;
  static HashMap<Integer, Boolean> c_v;


  public static void dfs(int curr){
    if (!vis[curr]){
      vis[curr] = true;
      c_v.put(curr, true);
      for (Integer node: adj.get(curr)){
        dfs(node);
      }
    }
  }

  public static void main(String[] args) throws java.io.IOException{
    FastIn sc = new FastIn();
    n = sc.readInt(); m = sc.readInt();
    adj = new ArrayList<ArrayList<Integer>>(n+1);
    threes = new ArrayList<ArrayList<Integer>>(n+1);
    twos = new ArrayList<ArrayList<Integer>>(n+1);
    ones = new ArrayList<Integer>(n+1);
    c_v = new HashMap<Integer, Boolean>();
    vis = new boolean[n+1];
    
    for (int i = 0; i <= n; i++) adj.add(new ArrayList<Integer>());

    for (int i = 0; i < m; i++){
      a = sc.readInt(); b = sc.readInt();
      adj.get(a).add(b);
      adj.get(b).add(a);
    }

    for (int i = 1; i <= n; i++){
      c_v.clear();
      if (!vis[i]){
        dfs(i);
        if (c_v.size() == 1) ones.add(i);
        else if (c_v.size() == 2) {
          ArrayList<Integer> temp = new ArrayList<Integer>();
          for (Integer node: c_v.keySet()) temp.add(node);
          twos.add(temp);
        } else if (c_v.size() > 3) out = false;
        else {
          ArrayList<Integer> temp = new ArrayList<Integer>();
          for (Integer node: c_v.keySet()) temp.add(node);
          threes.add(temp);
        }
      }
    }

    for (int i = 1; i < n; i++) if (!vis[i]) ones.add(i);
    if (out && (ones.size() == twos.size() || ((ones.size()-twos.size()) % 3 == 0 && ones.size() > twos.size()))){      
      int k = 0;
      for (ArrayList<Integer> triple : threes) System.out.println(triple.get(0) + " " + triple.get(1) + " " + triple.get(2));
      if (twos.size() > 0) for (; k < twos.size(); k++) System.out.println(twos.get(k).get(0) + " " + twos.get(k).get(1) + " " + ones.get(k));
      for (int i = k; i < ones.size(); i+=3) System.out.println(ones.get(i) + " " + ones.get(i+1) + " " + ones.get(i+2));
    }
    else System.out.println(-1);
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