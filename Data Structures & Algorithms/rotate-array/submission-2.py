class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        k %= n 
        
        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1 
                right -= 1

        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)
        
        return arr