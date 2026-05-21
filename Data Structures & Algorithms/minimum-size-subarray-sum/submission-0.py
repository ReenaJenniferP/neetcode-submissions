class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_len = float('inf')
        left = 0

        for right, v in enumerate(nums):
            window_sum += v

            while window_sum >= target:
                print(window_sum)
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

            
            
        return min_len if min_len != float('inf') else 0
