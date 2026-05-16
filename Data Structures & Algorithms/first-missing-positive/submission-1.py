class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = set([x for x in nums if x > 0])
        
        missing = 1
        while missing in arr:
            missing += 1 
        
        return missing 