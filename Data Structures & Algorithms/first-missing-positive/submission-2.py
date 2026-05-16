class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while (1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]):
                c = nums[i]- 1
                nums[i], nums[c] = nums[c], nums[i]

        print(nums)

        for i, v in enumerate(nums):
            if v != i+1:
                return i+1
        
        return n+1



