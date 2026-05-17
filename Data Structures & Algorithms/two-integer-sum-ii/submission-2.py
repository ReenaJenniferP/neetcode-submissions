class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i = 0
        j = len(arr) - 1

        while i < j:
            t = arr[i] + arr[j]

            if t == target:
                return [i+1, j+1]
            elif t < target:
                i += 1
            else:
                j -= 1

            
        