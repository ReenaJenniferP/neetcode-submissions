class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key in frequency:
            buckets[frequency[key]].append(key)

        res = []

        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                if k == 0:
                    return res
                res.append(num)
                k -= 1


        return res