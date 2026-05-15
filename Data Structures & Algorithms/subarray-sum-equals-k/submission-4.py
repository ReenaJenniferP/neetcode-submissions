class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix = defaultdict(int) 
        prefix[0] = 1
        currsum = 0

        for i in nums:
            currsum += i
            count += prefix[currsum-k]
            prefix[currsum] += 1
        
        return count