class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        copy_arr = arr
        curr_high = arr[len(arr) - 1]
        for idx in range(len(arr) - 2, -1, -1): 
            curr_high = max(curr_high, copy_arr[idx])
            copy_arr[idx] = curr_high
        
        for idx in range(0, len(arr) - 1):
            arr[idx] = copy_arr[idx + 1]
        
        arr[len(arr) - 1] = - 1

        return arr