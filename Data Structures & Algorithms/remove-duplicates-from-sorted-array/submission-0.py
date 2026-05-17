class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 1
        j = 1

        while j < len(arr) and i < len(arr):
            if arr[j] == arr[j-1]:
                j += 1
            else:
                arr[i] = arr[j]
                j += 1
                i += 1 
        
        return i
        

        


        