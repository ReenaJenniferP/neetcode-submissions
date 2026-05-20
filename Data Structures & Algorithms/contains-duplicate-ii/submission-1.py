class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

# have window of k length
# check if any element in it has a freq >= 2 

        window = set()
        l = 0

        for r, v in enumerate(nums):
            if v in window:
                return True

            window.add(v)
            
            if (r - l + 1) > k:
                window.remove(nums[l])
                l += 1
        
        return False
