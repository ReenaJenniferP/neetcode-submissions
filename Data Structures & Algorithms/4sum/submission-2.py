class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            needed = target - nums[i]

            for j in range(i+1, n):

                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                remain = needed - nums[j]
                k = j+1
                l = n-1
                
                while k < l:
                    s = nums[k] + nums[l]

                    if s == remain:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        while k<l and nums[k] == nums[k+1]:
                            k += 1
                        
                        while k<l and nums[l] == nums[l-1]:
                            l -= 1
                        
                        k += 1
                        l -= 1
                    
                    elif s < remain:
                        k += 1

                    else:
                        l -= 1
                
        return res