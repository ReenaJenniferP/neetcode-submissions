class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0]*26
        freq_sub = [0]*26

        for i, v in enumerate(s1):
            idx = ord(v) - ord('a')
            freq_s1[idx] += 1

        left = 0

        for right, v in enumerate(s2):
            print(s2[left:right+1])

            idx = ord(v) - ord('a')
            freq_sub[idx] += 1 
            
            if right - left == len(s1):
                idx = ord(s2[left]) - ord('a')
                freq_sub[idx] -= 1 
                left += 1
            
            if freq_sub == freq_s1:
                return True
        
        return False
            


            
                