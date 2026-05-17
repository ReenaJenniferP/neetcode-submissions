class Solution:
    def merge(self, arr: List[int], m: int, nums2: List[int], n: int) -> None:
        start = m
        for i in nums2:
            j = start
            while j > 0 and arr[j-1] > i:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = i
            start += 1
                
        