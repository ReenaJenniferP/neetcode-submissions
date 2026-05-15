class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0]*(n+1)

        for i in range(1, n+1):
            prefix[i] += prefix[i-1] + nums[i-1]

        d = defaultdict(list)

        for i, v in enumerate(prefix):
            d[v].append(i)
        
        count = 0

        for i, v in enumerate(prefix):
            if (v-k) in d:
                for ind in d[v-k]:
                    if ind < i:
                        count += 1

        return count
        