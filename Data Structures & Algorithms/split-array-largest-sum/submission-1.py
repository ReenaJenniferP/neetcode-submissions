class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low+high)//2

            created = 1
            s = 0
            for i in nums:
                if s + i > mid:
                    created += 1
                    s = 0
                s += i 
            
            if created > k:
                low = mid + 1
            else:
                high = mid 
            
        return low


