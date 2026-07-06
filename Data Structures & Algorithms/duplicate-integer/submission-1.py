class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_dict = set()

        for num in nums:
            if num in number_dict:
                return True
            number_dict.add(num)
        
        return False

