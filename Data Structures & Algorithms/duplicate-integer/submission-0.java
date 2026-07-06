class Solution {
    public boolean hasDuplicate(int[] nums) {
        var hashSet = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++) {
            if (hashSet.contains(nums[i])) {
                return true;
            } else {
                hashSet.add(nums[i]);
            }
        }
        return false;
    }
}
