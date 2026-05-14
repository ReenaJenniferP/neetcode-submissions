class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key in frequency:
            buckets[frequency[key]].append(key)

        idx = len(nums)-1
        res = []

        while k > 0:
            for i in buckets[idx]:
                res.append(i)
                k -= 1
            idx -= 1

        return res