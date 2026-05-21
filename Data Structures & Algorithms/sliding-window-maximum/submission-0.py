class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        window = []
        max_list = []

        for right, v in enumerate(nums):
            window.append(v)

            if (right-left+1) > k:
                window.pop(0)
                left += 1

            if (right-left+1) == k:
                max_list.append(max(window))
            
        return max_list

