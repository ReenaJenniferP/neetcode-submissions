class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        start = 0
        length = 0

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[start])
                start += 1
            
            seen.add(c)

            length = max(length, i-start+1)
        
        return length

            


