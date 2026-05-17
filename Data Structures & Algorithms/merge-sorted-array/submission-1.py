class Solution:
    def merge(self, arr: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            j = m
            while j > 0 and arr[j-1] > i:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = i
            m += 1
                
        