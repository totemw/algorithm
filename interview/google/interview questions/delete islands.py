"""
Given a binary grid where 0 represents water and 1 represents land.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
Delete all islands except their borders. A border is land adjacent to water.
You may assume all four edges of the grid are surrounded by water.

Example 1:

Input:
[[0, 0, 0, 1, 1, 1],
 [0, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]]

Output:
[[0, 0, 0, 1, 1, 1],
 [0, 0, 0, 1, 0, 1],
 [1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1]]

 dfs

 public class Main {

    public static void main(String[] args) {
        boolean [][] visited = new boolean[grid.length][grid[0].length];
        boolean [][] changed = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    dfs(grid,i,j,visited,changed);
                }
            }
        }
    }
  private static void dfs(int[][] grid, int i, int j, boolean[][] visited, boolean[][] changed) {
        if(i<0 || i>=grid.length || j<0 || j>=grid[0].length || visited[i][j]) {
            return;
        }
        visited[i][j] = true;
        if(grid[i][j] == 1) {
            if(!isBorder(grid,i,j,changed)) {
                grid[i][j] = 0;
                changed[i][j] = true;
            }
        }
        dfs(grid,i+1,j,visited,changed);
        dfs(grid,i-1,j,visited,changed);
        dfs(grid,i,j + 1,visited,changed);
        dfs(grid,i,j - 1,visited,changed);
}
    private static boolean isBorder(int [][] grid, int i, int j, boolean[][] changed) {
        if (i - 1 < 0) return true;
        if (i + 1 == grid.length) return true;
        if (j - 1 < 0) return true;
        if (j + 1 == grid[0].length) return true;
        if(grid[i-1][j] == 0 && !changed[i-1][j]) return true;
        if(grid[i+1][j] == 0 && !changed[i+1][j]) return true;
        if(grid[i][j-1] == 0 && !changed[i][j-1]) return true;
        if(grid[i][j+1] == 0 && !changed[i][j+1]) return true;
        return false;
    }
}

"""