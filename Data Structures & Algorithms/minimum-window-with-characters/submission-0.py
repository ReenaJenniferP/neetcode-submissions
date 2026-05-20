class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = defaultdict(int)
        need = defaultdict(int)
        
        left = 0

        ml = float('inf')
        cand = ""

        for char in t:
            need[char] += 1
        
        have = 0
        required = len(need)

        for right, v in enumerate(s):
            if v in need:
                seen[v] += 1
                if seen[v] == need[v]:
                    have += 1 

            while have == required:
                length = right - left + 1
                if length < ml:
                    ml = length
                    cand = s[left:right+1]

                char = s[left]
                if char in need:
                    seen[char] -= 1
                    if seen[char] < need[char]:
                        have -= 1
                left += 1
            
        return cand
                
                





            