class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = None
        b = None
    
        ca = 0
        cb = 0
        for i in nums:
            if i == a:
                ca += 1
            elif i == b:
                cb += 1
            elif ca == 0:
                a = i
                ca += 1
            elif cb == 0:
                b = i
                cb += 1
            else:
                ca -= 1 
                cb -= 1

        res = []
        for i in [a, b]:
            if i != None and nums.count(i) > len(nums)//3:
                res.append(i)
                
        return res
