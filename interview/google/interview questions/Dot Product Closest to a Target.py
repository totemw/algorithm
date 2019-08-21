"""
 Dot Product Closest to a Target
 Given an array of integers and target value, return the output comprising of 0's and 1's such that
largest dot product (of input and the output) is equal or less than target value.
Input: [1, 2, 2, 1], target = 3
Output: [1, 1, 0, 0] or [1, 0, 1, 0]
=> subset sum close to target: find all
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

or direct sorted and 2 sum
    nums = sorted(nums, key=lambda x:x[1])
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l][1]+nums[r][1] == target:
            return sorted([nums[l][0]+1, nums[r][0]+1])
        elif nums[l][1]+nums[r][1] < target:
            l += 1
        else:
            r -= 1
"""
