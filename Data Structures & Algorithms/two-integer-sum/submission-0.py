class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_map = dict() 

       for idx, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target- num], idx]
            num_map[num] = idx