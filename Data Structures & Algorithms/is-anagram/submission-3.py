class Solution:
    def construct_arr(self, word: str) -> List[int]:
        arr = [0]  * 26
        for letter in word:
            arr[ord(letter) - ord('a')] += 1
        return arr

    def isAnagram(self, s: str, t: str) -> bool:
        return self.construct_arr(s) == self.construct_arr(t)