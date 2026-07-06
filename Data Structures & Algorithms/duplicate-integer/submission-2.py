class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_dict = set(nums)

        return len(nums) != len(number_dict)


