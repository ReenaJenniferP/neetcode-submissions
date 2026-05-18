class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []

        for x in range(n):
            if x > 0 and nums[x] == nums[x-1]:
                continue

            target = -nums[x] 

            i, j = x+1, n-1
            
            while i < j:

                s = nums[i] + nums[j]

                if s == target:
                    res.append([nums[i], nums[j], nums[x]])

                    while i < j and nums[i] == nums[i+1]:
                            i += 1 
                
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1


                elif s < target:
                    i += 1
                
                else:
                    j -= 1


        return res