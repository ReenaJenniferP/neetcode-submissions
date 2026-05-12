class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        check = strs[0]
        for char in check:
            for word in strs:
                if count >= len(word) or word[count] != char:
                    return check[0:count]
            count += 1
        return check