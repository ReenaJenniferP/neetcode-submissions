class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            for j in range(i, len(numbers)):
                if numbers[j] + numbers[i] == target:
                    return [i+1, j+1]        
            
        