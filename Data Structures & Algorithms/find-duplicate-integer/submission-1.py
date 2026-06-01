class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        intersection = slow
        start = 0

        while start != intersection:
            start = nums[start]
            intersection = nums[intersection]

        return start
        