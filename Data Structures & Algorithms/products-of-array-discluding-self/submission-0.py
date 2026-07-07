class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        for idx, num in enumerate(nums):
            if zero_count == 0:
                nums[idx] = total_product // num
            elif zero_count ==1:
                nums[idx] = total_product if num == 0 else 0
            else:
                nums[idx] = 0
        return nums
