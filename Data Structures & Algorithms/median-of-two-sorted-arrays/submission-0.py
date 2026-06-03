class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)

        if len(B) < len(A):
            A, B = B, A

        low, high = 0, len(A) - 1

        while True:
            i = (low+high)//2
            j = total//2 - i - 2  

            Aleft = A[i] if i >= 0 else -float('inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else -float('inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                a = max(Aleft, Bleft)
                b = min(Aright, Bright)

                if total % 2 == 0:
                    return (a+b)/2

                else:
                    return b

            elif Bleft > Aright:
                low = i + 1
            
            else:
                high = i - 1