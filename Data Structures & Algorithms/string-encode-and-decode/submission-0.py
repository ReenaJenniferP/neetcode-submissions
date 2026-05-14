class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = result + str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        num = ""
        i = 0

        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            else:
                i += 1
                length = int(num)
                num = ""
                strs.append(s[i:i+length])
                i += length
        
        return strs