class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = dict()
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        
        ans = [key for (value, key) in sorted([(value, key) for key, value in num_map.items()])]
        ans = ans[len(ans)-k::]

        return ans