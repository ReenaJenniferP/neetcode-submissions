class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def partition(arr, low, high):
            idx = random.randint(low, high)
            arr[high], arr[idx] = arr[idx], arr[high]
            pivot = arr[high]
            i = low
            for j in range(low, high):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
            arr[i], arr[high] = arr[high], arr[i]
            return i

        def quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort(arr, low, pi-1)
                quick_sort(arr, pi+1, high)
        
        quick_sort(nums, 0, len(nums)-1)
        return nums