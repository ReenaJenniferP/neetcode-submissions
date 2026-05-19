class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = [0]*26
        ml = 0

        for right, v in enumerate(s):
            freq[ord(s[right]) - ord('A')] += 1

            while ((right - left + 1) - max(freq)) > k:
                freq[ord(s[left]) - ord('A')] -= 1 
                left += 1
            
            ml = max(ml, right-left+1)

        return ml