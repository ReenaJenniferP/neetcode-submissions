class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        window = []
        heapq.heapify(window)

        max_list = []

        for right, v in enumerate(nums):
            heapq.heappush(window, (-1*v, right))
            
            while (right-left+1) > k:
                left += 1

            while window[0][1] < left:
                heapq.heappop(window)
            
            if (right-left+1) == k:
                max_list.append(-1*window[0][0])
            
        return max_list

