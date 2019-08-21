"""
1 array （一维）
backtrack 三种类型： subset / permutation / partition

(1) subset
public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, 0);
    return list;
}

private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
    ／／每次产生一个新的list，就直接加到结果里
    list.add(new ArrayList<>(tempList));
    ／／注意start要作为一个循环的开头，每次start加一，每个start开始都是一组set，里面包含当前的start，和后面出现或者不出现的每个数字
    for(int i = start; i < nums.length; i++){
        tempList.add(nums[i]);
        backtrack(list, tempList, nums, i + 1);
        tempList.remove(tempList.size() - 1);
    }
}

subset with duplicate (sort first)

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start){
    list.add(new ArrayList<>(tempList));
    for(int i = start; i < nums.length; i++){
        if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
        tempList.add(nums[i]);
        backtrack(list, tempList, nums, i + 1);
        tempList.remove(tempList.size() - 1);
    }
}

(2) permutation
public List<List<Integer>> permute(int[] nums) {
   List<List<Integer>> list = new ArrayList<>();
   // Arrays.sort(nums); // not necessary
   //因为顺序重要 元素的数量不重要，所以我们就不使用start变量去控制有多少元素存在于templist中
   backtrack(list, new ArrayList<>(), nums);
   return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
   if(tempList.size() == nums.length){
      list.add(new ArrayList<>(tempList));
   } else{
      for(int i = 0; i < nums.length; i++){
         if(tempList.contains(nums[i])) continue; // element already exists, skip
         tempList.add(nums[i]);
         backtrack(list, tempList, nums);
         tempList.remove(tempList.size() - 1);
      }
   }
}

permutation with duplicate (sort first)
private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean [] used){
    if(tempList.size() == nums.length){
        list.add(new ArrayList<>(tempList));
    } else{
        for(int i = 0; i < nums.length; i++){
            if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
            used[i] = true;
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, used);
            used[i] = false;
            tempList.remove(tempList.size() - 1);
        }
    }
}

(3) subset to target sum: can reuse same element

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
    if(remain < 0) return;
    else if(remain == 0) list.add(new ArrayList<>(tempList));
    else{
        for(int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1);
        }
    }
}

subset sum: cannot reuse same element

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
    if(remain < 0) return;
    else if(remain == 0) list.add(new ArrayList<>(tempList));
    else{
        for(int i = start; i < nums.length; i++){
            if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }
}

(4) partition (similar to subset)

public void backtrack(List<List<String>> list, List<String> tempList, String s, int start){
   if(start == s.length())
      list.add(new ArrayList<>(tempList));
   else{
      for(int i = start; i < s.length(); i++){
         if(isPalindrome(s, start, i)){
            tempList.add(s.substring(start, i + 1));
            backtrack(list, tempList, s, i + 1);
            tempList.remove(tempList.size() - 1);
         }
      }
   }
}

(5) Combination
给定两个整数n和k，求1..n中取k个数构成的所有组合。
def backtrack(n, k, tmp, res, start):
    if len(tmp) == k:
        res.append(list(tmp))
        return
    for i in range(start, n + 1, 1):
        if len(tmp) < k:
            tmp.append(i)
            backtrack(n, k, tmp, res, i + 1)
            tmp.pop()

"""

# medium
# generate parenthesis: 22
#recursion rule 就是判断left，right的count啦，直到满足right == n
def dfs(self, temp, left, right, res, n):
    if right==n:
        res.append(temp)
    if left < n:
        self.dfs(temp+'(', left+1, right, res, n)
    if right < left:
        self.dfs(temp+')', left, right+1, res, n)

# Generalized Abbreviation 320
"""
Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
def backtrack(res, word, pos, string, count):
    if pos == len(word):
        if count > 0:
            string += str(count)
        res.append(string)
    else:
        backtrack(res,word,pos+1,string,count+1)
        # 这个track保证了index每次不断加1 从而在base的时候输出，然后每一次count同时加1，为了记录count
        backtrack(res, word, pos+1, string + (str(count) if count>0 else "")+ word[pos], 0)
        # 这个是为了退一步，先保存当前的count数字，然后因为数字不能连续，所以+word【index】，同时把count清0

# dot product 17
# [[1,2,3][4,5,6]...]
def backtrack(arr, start, res, tmp, n):
    if tmp.len == n:
        res.append(list(tmp))
    for i in range(start, len(arr), 1):
        for j in arr[i]:
            tmp.append(j)
            backtrack(arr, i + 1, res, tmp, n)
            tmp.pop()


"""
2. 2D matrix
"""
# word search 212
def dfs(matrix, i, j, string):
    if string == "":
        return True
    m = len(matrix)
    n = len(matrix[0])
    directions = [(0,-1), (1, 0), (0, 1), (-1, 0)]
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] == string[0]:  # and other condition
            dfs(matrix, x, y, string[1:])
    return False

# word ladder 126/127
# using bfs

# unique paths 980 63
# def dfs(r, c, todo):
#     todo -= 1
#     if todo < 0: return
#     if r == tr and c == tc:
#         if todo == 0:
#             self.ans += 1
#         return
#
#     grid[r][c] = -1
#     for nr, nc in neighbors(r, c):
#         dfs(nr, nc, todo)
#     grid[r][c] = 0

# Squareful Arrays 996
import math


class Solution(object):
    def is_square(self, i):
        return i == math.sqrt(i) ** 2

    def dfs(self, A, res, tmp):
        if len(tmp) == len(A):
            res.append(list(tmp))
        for i in range(len(A)):
            if A[i] in tmp:
                continue
            if tmp and i > 0 and not self.is_square(A[i] + tmp[-1]):
                continue
            tmp.append(A[i])
            self.dfs(A, res, tmp)
            tmp.pop()

    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = []
        self.dfs(A, res, [])
        print(res)
