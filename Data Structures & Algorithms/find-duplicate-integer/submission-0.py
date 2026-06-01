class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        intersection = slow
        start = 0

        while start != intersection:
            start = nums[start]
            intersection = nums[intersection]

        return start
        