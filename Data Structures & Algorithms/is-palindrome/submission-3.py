class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        print(s)
        
        start = 0
        end = n-1

        while start < end:
            a = s[start].isalnum()
            b = s[end].isalnum()

            if a and b:
                if s[end] != s[start]:
                    return False
                start += 1
                end -= 1
            
            else:
                if not a:
                    start += 1
                if not b:
                    end -= 1
            
        return True

            