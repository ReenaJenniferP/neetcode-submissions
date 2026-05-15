class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        nums = set(arr)

        mlen = 0

        for i in nums:
            if i-1 not in nums:
                clen = 0
                while clen + i in nums:
                    clen += 1
                
                mlen = max(mlen, clen)

        return mlen
