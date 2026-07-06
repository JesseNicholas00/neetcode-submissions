class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = ["".join(sorted(x))for x in strs]
        map_anagram = dict() 

        for idx in range(len(strs)):
            if sorted_str[idx] not in map_anagram:
                map_anagram[sorted_str[idx]] = [strs[idx]]
            else:
                map_anagram[sorted_str[idx]].append(strs[idx])
        
        ans = []
        for value in map_anagram.values():
            ans.append(value)
        
        return ans