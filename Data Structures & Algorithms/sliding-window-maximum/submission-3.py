class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        q = deque()
        max_list = []

        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if left > q[0]:
                q.popleft()

            if (right+1-left) == k:
                max_list.append(nums[q[0]])
                left += 1
            
        return max_list

