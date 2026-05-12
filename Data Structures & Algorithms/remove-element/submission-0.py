class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        i=0
        for j in range(len(arr)):
            if arr[j] != val:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        return i