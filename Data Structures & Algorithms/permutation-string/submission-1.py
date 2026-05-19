class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        freq_s1 = [0]*26
        freq_sub = [0]*26

        for v in s1:
            freq_s1[ord(v) - ord('a')] += 1

        left = 0

        for right, v in enumerate(s2):

            freq_sub[ord(v) - ord('a')] += 1 
            
            if right - left == len(s1):
                freq_sub[ord(s2[left]) - ord('a')] -= 1 
                left += 1
            
            if freq_sub == freq_s1:
                return True
        
        return False
            


            
                