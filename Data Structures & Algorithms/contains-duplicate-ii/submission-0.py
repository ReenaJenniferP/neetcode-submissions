class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

# have window of k length
# check if any element in it has a freq >= 2 

        window = defaultdict(int)
        l = 0

        for r, v in enumerate(nums):
            window[v] += 1

            if (r - l) > k:
                window[nums[l]] -= 1
                l += 1

            for i in window:
                if window[i] == 2:
                    return True
        
        return False
