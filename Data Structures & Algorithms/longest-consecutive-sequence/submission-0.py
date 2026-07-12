class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection = set(nums)
        ans = 0
        for num in nums:
            if (num - 1) not in collection:
                candidate = 1
                temp = num
                while True:
                    if (temp + 1) in collection:
                        candidate += 1
                        temp += 1
                    else:
                        break
                ans = max(ans, candidate)

        return ans
        