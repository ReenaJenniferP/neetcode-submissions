class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = [0]*26
        ml = 0
        mf = 0

        for right, v in enumerate(s):
            idx = ord(v) - ord('A')
            freq[idx] += 1

            mf = max(mf, freq[idx])

            while ((right - left + 1) - mf) > k:
                freq[ord(s[left]) - ord('A')] -= 1 
                left += 1
            
            ml = max(ml, right-left+1)

        return ml