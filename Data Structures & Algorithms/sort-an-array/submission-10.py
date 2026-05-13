class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, low, mid, high):
            a = arr[low:mid+1]
            b = arr[mid+1:high+1]

            i, j, k = 0, 0, low
            n1 = len(a)
            n2 = len(b)

            while i < n1 and j < n2:
                if a[i] < b[j]:
                    arr[k] = a[i]
                    i += 1
                else:
                    arr[k] = b[j]
                    j += 1
                k += 1

            if i < n1:
                arr[k:high+1] = a[i:]
            
            if j < n2:
                arr[k:high+1] = b[j:]

        def merge_sort(arr, low, high):
            if low < high:
                mid = (low+high)//2
                merge_sort(arr, low, mid)
                merge_sort(arr, mid+1, high)
                merge(arr, low, mid, high)
        
        merge_sort(nums, 0, len(nums)-1)
        return nums